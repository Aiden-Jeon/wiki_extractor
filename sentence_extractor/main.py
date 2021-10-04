import typer

import sentence_extractor
from sentence_extractor import index_extractor, sentence_extactor
from wikiextractor.WikiExtractor import main

app = typer.Typer(help="Sentence Extractor for Wikipedia")

@app.command()
def version() -> None:
    """Show version"""
    typer.secho(sentence_extractor.__version__)


def entry_point() -> None:
    """sentence extractor CLI entrypoint"""

    # Sub-commands
    app.add_typer(index_extractor.app, name="idxbook")
    app.add_typer(sentence_extactor.app, name="sentence")
    typer_click_object = typer.main.get_command(app)
    typer_click_object()


if __name__ == "__main__":
    entry_point()
