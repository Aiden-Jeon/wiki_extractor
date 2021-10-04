from typing import Union, Dict, Any
from pathlib import Path

import typer

app = typer.Typer(help="indexbook extracting commands")


def index_extractor(path: Union[str, Path], folder: str, wiki: str) -> Dict[str, Any]:
    index = {}
    with open(path, "r") as f:
        for line_num, line in enumerate(f):
            line = line.strip()
            # start of doc
            if line.startswith("<doc id"):
                title = line.split("title=")[-1]
                title = title.replace('"', "").replace(">", "")
                start_num = line_num
            # end of doc
            elif line.endswith("doc>"):
                end_num = line_num
                index[title] = (folder, wiki, start_num, end_num)
    return index


def make_idxbook(root_dir: str, save_dir: str):
    root_dir = Path(root_dir)
    indexes = {}
    for folder_dir in root_dir.glob("*"):
        folder = folder_dir.name
        if folder_dir.is_dir():
            for wiki_dir in folder_dir.glob("wiki*"):
                wiki = wiki_dir.name
                index = index_extractor(wiki_dir, folder, wiki)
                indexes.update(index)

    save_dir = Path(save_dir)
    with open(save_dir / "idxbook.tsv", "w") as f:
        header = ["name", "folder", "wiki", "line_start", "line_end"]
        line = "\t".join(header)
        f.write(line)
        f.write("\n")
        for name, idx in indexes.items():
            line = "\t".join([name] + list(map(str, idx)))
            f.write(line)
            f.write("\n")


@app.command()
def extract(
    data_dir: str = typer.Option(..., help="Path for extracted wiki"),
    save_dir: str = typer.Option("./", help="Path to save idxbook"),
):
    make_idxbook(data_dir, save_dir)
