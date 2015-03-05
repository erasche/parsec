import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('histories_get_status')
@click.argument("history_id", type=str)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id):
    """Returns the state of this history
    """
    return ctx.gi.histories.get_status(history_id)
