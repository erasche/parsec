
import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_quota')
@options.galaxy_instance()


@click.option(
    "--quota_id",
    help="Encoded quota ID",
    type=str
)
@click.option(
    "--deleted",
    help="Search for quota in list of ones already marked as deleted",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, quota_id=False, deleted=False):
    """Display information on a quota
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.quotas.show_quota(quota_id=quota_id, deleted=deleted)