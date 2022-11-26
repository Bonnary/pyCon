from editor import *
import typer
from typing import List

app = typer.Typer(add_completion=False)


@app.command()
def con(
    image_name: List[str] = typer.Argument(...,
                                           help="Image name", show_default=False),
    extension_convert_to: str = typer.Argument(
        ..., help="Extension name [Example 'png']", show_default=False),
):
    """Converts image to other formats."""
    for img in image_name:
        rename = "Converted_" + img
        convert(os.getcwd(), img, extension_convert_to, rename)
    # raise typer.Exit()


@app.command()
def rsp(
    image_name: List[str] = typer.Argument(...,
                                           help="Image name", show_default=False),
    scale_percent: int = typer.Argument(...,
                                        help="Input size percent", show_default=False),
):
    """Resizes image by percentage."""
    for img in image_name:
        rename = "Converted_" + img
        resize_percent(os.getcwd(), img, scale_percent, rename)


@app.command()
def rs(
    image_name: List[str] = typer.Argument(...,
                                           help="Image name", show_default=False),
    width: int = typer.Argument(...,
                                help="Image width", show_default=False),
    height: int = typer.Argument(...,
                                 help="Image height", show_default=False),
):
    """Resizes image by width and height"""
    for img in image_name:
        rename = "Converted_" + img
        resize(os.getcwd(), img, width, height, rename)


@app.command()
def bw(
    image_name: List[str] = typer.Argument(...,
                                           help="Image name", show_default=False),
):
    """Converts image to black and white"""
    for img in image_name:
        rename = "Converted_" + img
        black_and_white(os.getcwd(), img, rename)


@app.command()
def inv(
    image_name: List[str] = typer.Argument(...,
                                           help="Image name", show_default=False),
):
    """Converts image to invert image"""
    for img in image_name:
        rename = "Converted_" + img
        invert(os.getcwd(), img, rename)


@app.command()
def r(
    image_name: List[str] = typer.Argument(...,
                                           help="Image name", show_default=False),
    angle: str = typer.Argument(...,
                                help="rotate angle ['left', 'right','flip-down','flip-x','flip-down-x']", show_default=False),
):
    """Rotates image"""
    for img in image_name:
        rename = "Converted_" + img
        rotate(os.getcwd(), img, angle, rename)


@app.command()
def blur(
    image_name: List[str] = typer.Argument(...,
                                           help="Image name", show_default=False),
    blur_value: str = typer.Argument(...,
                                     help="blur value (positive integer number)", show_default=False),
):
    """Blur image"""
    for img in image_name:
        rename = "Converted_" + img
        blur(os.getcwd(), img, blur_value, rename)


@app.command()
def pencil(
    image_name: List[str] = typer.Argument(...,
                                           help="Image name", show_default=False),
):
    """Converts image to pencil sketch art image"""
    for img in image_name:
        rename = "Converted_" + img
        pencilSketch(os.getcwd(), img, rename)


@app.callback()
def main():
    """For convert multiple images"""


if __name__ == "__main__":
    app()
