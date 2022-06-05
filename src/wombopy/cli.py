from typing import Optional
from venv import create

import typer

from wombopy import __app_name__, __version__, create, identify
from wombopy.logging import wombolog
from wombopy.core.generation import show_img

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.command(help="Create an image from wombo.art")
def run(
    open_result: Optional[bool] = typer.Option(
        False, "--show", "-s", help="Show back the image."
    ),
    debug: Optional[bool] = typer.Option(
        True, "--debug", help="Show logs."
    ),
    identify_key: str = typer.Argument(...),
    prompt: str = typer.Argument(...),
    style: int = typer.Argument(...),
) -> None:
    wombolog.propagate = debug
    
    wombolog.info(f"Prompt: {prompt}\tStyle: {style}")
    wombolog.info("Starting...")

    res = identify(identify_key=identify_key)
    img_uri = create(res["id_token"], prompt, style)
    
    if open_result:
        show_img(img_uri)

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
