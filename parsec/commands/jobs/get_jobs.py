import click
import json
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_jobs')


@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Get the list of jobs of the current user.
    """
    return ctx.gi.jobs.get_jobs()
