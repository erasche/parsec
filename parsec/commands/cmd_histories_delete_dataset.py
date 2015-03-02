import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_delete_dataset')
@options.galaxy_instance()
@click.argument("history_id", type=str)
@click.argument("dataset_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, history_id, dataset_id):
    """Mark corresponding dataset as deleted.
    """
    return ctx.gi.histories.delete_dataset(history_id, dataset_id)
