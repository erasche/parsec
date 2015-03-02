import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('workflows_import_workflow_json')
@options.galaxy_instance()
@click.argument("workflow_json", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, workflow_json):
    """Imports a new workflow given a json representation of a previously exported workflow.
    """
    return ctx.gi.workflows.import_workflow_json(workflow_json)
