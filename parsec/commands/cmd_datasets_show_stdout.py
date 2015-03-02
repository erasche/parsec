import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('datasets_show_stdout')
@options.galaxy_instance()
@click.argument("dataset_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, dataset_id):
    """Display stdout output of a dataset.
    """
    return ctx.gi.datasets.show_stdout(dataset_id)
