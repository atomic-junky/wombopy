from typing import Optional

import typer

from wombopy import __app_name__, __version__, generate
from wombopy.core import identify

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.command(help="Create an image from wombo.art")
def run(open_result: Optional[bool] = typer.Option(
    None,
    "--show",
    "-s",
    help="Show back the image"
),
        identify_key: str = typer.Argument(...),
        prompt: str = typer.Argument(...),
        style: int = typer.Argument(...)
) -> None:
    typer.secho(f"Prompt: {prompt}\tStyle: {style}")
    typer.secho("Starting...")

    res = identify(identify_key=identify_key)
    generate(res['id_token'], prompt, style, open_result)

    return


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Show the application's version and exit.",
            callback=_version_callback,
            is_eager=True,
        )
) -> None:
    return
