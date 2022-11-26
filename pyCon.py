from editor import *
import typer
from typing import Optional
import allpyCon

app = typer.Typer(add_completion=False)
app.add_typer(allpyCon.app, name="all")

__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        typer.echo(f"pyCon CLI Version: {__version__}")
        raise typer.Exit()


@app.command()
def con(
    image_name: str = typer.Argument(...,
                                     help="Image name", show_default=False),
    extension_convert_to: str = typer.Argument(
        ..., help="Extension name [Example 'png']", show_default=False),
    rename: str = typer.Argument(
        None, help="New image name without extension", show_default=False)
):
    """Converts image to other formats."""
    convert(os.getcwd(), image_name, extension_convert_to, rename)
    # raise typer.Exit()


@app.command()
def rsp(
    image_name: str = typer.Argument(...,
                                     help="Image name", show_default=False),
    scale_percent: int = typer.Argument(...,
                                        help="Input size percent", show_default=False),
    rename: str = typer.Argument(
        None, help="rename image and image extension", show_default=False)
):
    """Resizes image by percentage."""
    resize_percent(os.getcwd(), image_name, scale_percent, rename)


@app.command()
def rs(
    image_name: str = typer.Argument(...,
                                     help="Image name", show_default=False),
    width: int = typer.Argument(...,
                                help="Image width", show_default=False),
    height: int = typer.Argument(...,
                                 help="Image height", show_default=False),
    rename: str = typer.Argument(
        None, help="rename image and image extension", show_default=False)
):
    """Resizes image by width and height"""
    resize(os.getcwd(), image_name, width, height, rename)


@app.command()
def bw(
    image_name: str = typer.Argument(...,
                                     help="Image name", show_default=False),
    rename: str = typer.Argument(
        None, help="rename image and image extension", show_default=False)
):
    """Converts image to black and white"""
    black_and_white(os.getcwd(), image_name, rename)


@app.command()
def inv(
    image_name: str = typer.Argument(...,
                                     help="Image name", show_default=False),
    rename: str = typer.Argument(
        None, help="rename image and image extension", show_default=False)
):
    """Converts image to invert image"""
    invert(os.getcwd(), image_name, rename)


@app.command()
def r(
    image_name: str = typer.Argument(...,
                                     help="Image name", show_default=False),
    angle: str = typer.Argument(...,
                                help="rotate angle ['left', 'right','flip-down','flip-x','flip-down-x']", show_default=False),
    rename: str = typer.Argument(
        None, help="rename image and image extension", show_default=False)
):
    """Rotates image"""
    rotate(os.getcwd(), image_name, angle, rename)


@app.command()
def blur(
    image_name: str = typer.Argument(...,
                                     help="Image name", show_default=False),
    blur_value: str = typer.Argument(...,
                                     help="blur value (positive integer number)", show_default=False),
    rename: str = typer.Argument(
        None, help="rename image and image extension", show_default=False)
):
    """Blur image"""
    blur(os.getcwd(), image_name, blur_value, rename)


@app.command()
def pencil(
    image_name: str = typer.Argument(...,
                                     help="Image name", show_default=False),
    rename: str = typer.Argument(
        None, help="rename image and image extension", show_default=False)
):
    """Converts image to pencil sketch art image"""
    pencilSketch(os.getcwd(), image_name, rename)


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, "-v", "--version", help="print version number and exit", callback=version_callback
    ),
):
    """pyCon is a cli too for converting image."""


if __name__ == "__main__":
    app()
