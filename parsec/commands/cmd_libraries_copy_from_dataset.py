import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_copy_from_dataset')
@options.galaxy_instance()
@click.argument("dataset_id", type=str)
@click.argument("message", type=str)

@click.option(
    "--library_id",
    help="id of the library where to place the uploaded file. If not provided, the root library will be used",
    type=str
)
@click.option(
    "--folder_id",
    help="id of the folder where to place the uploaded files. If not provided, the root folder will be used",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, dataset_id, message, library_id="", folder_id=""):
    """Copy a Galaxy dataset into a library.
    """
    return ctx.gi.libraries.copy_from_dataset(dataset_id, message, library_id=library_id, folder_id=folder_id)
