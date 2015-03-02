import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('users_create_local_user')
@options.galaxy_instance()
@click.argument("username", type=str)
@click.argument("user_email", type=str)
@click.argument("password", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, username, user_email, password):
    """Create a new Galaxy user.
    """
    return ctx.gi.users.create_local_user(username, user_email, password)
