
import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('create_history_tag')
@options.galaxy_instance()

@click.argument("history_id", type=str)
@click.argument("tag", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, history_id, tag):
    """Create history tag
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.histories.create_history_tag(history_id, tag)