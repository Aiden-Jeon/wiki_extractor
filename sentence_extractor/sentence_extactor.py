from typing import List
import linecache
from pathlib import Path

import pandas as pd
import typer

app = typer.Typer(help="sentence extracting commands")


def load_idxbook(idx_path: str) -> pd.DataFrame:
    idx_path = Path(idx_path)
    idxbook = pd.read_csv(idx_path, delimiter="\t")
    idxbook = idxbook.set_index("name")
    return idxbook


def extract_lines(name: str, idxbook: pd.DataFrame, data_dir: str) -> List[str]:
    lines = []
    try:
        value = idxbook.loc[name]
        file_dir = Path(data_dir) / value["folder"] / value["wiki"]
        for line_no in range(value[2] + 2, value[3]):
            line = linecache.getline(str(file_dir), line_no)
            lines += [line.strip()]
    except KeyError as e:
        print(f"{e} is not valid name.")
    return lines


def extarct_sentences(lines: List[str], min_line_length: int) -> List[str]:
    import kss

    sentence_list = map(kss.split_sentences, lines)
    sentences = []
    for sentence in sentence_list:
        for line in sentence:
            if len(line) > min_line_length:
                sentences.append(line)
    return sentences


def dump(name: str, sentences: List[str], save_dir: str) -> None:
    save_dir = Path(save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)
    with open(save_dir / f"{name}.txt", "w") as f:
        for sentence in sentences:
            f.write(sentence)
            f.write("\n")


@app.command()
def extract(
    name: str = typer.Option(..., help="Name to extract"),
    idxbook: str = typer.Option(..., help="Path for idxbook"),
    data_dir: str = typer.Option(..., help="Path for extracted wiki"),
    save_dir: str = typer.Option(..., help="Path to save extracted wiki"),
    kss: bool = typer.Option(False, is_flag=True, help="Path to save extracted wiki"),
    line_length: int = typer.Option(10, help="Skip sentence which is smaller than given length"),
):
    loaded_idxbook = load_idxbook(idxbook)
    lines = extract_lines(name, loaded_idxbook, data_dir)
    if len(lines) > 0 and kss:
        lines = extarct_sentences(lines, line_length)
    dump(name, lines, save_dir)
