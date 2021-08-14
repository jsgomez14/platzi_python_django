import click
from clients import commands as clients_commands

CLIENTS_TABLE = 'C:/Users/JuanseDesktop/Documents/Courses/platzi_python_django/crud_creation_course/platzi_ventas_2/clients.csv'

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_TABLE

cli.add_command(clients_commands.all)