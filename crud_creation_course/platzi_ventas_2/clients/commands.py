import click
from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n','--name',
              type=str,
              prompt=True,
              help='The client\'s name')
@click.option('-c','--company',
              type=str,
              prompt=True,
              help='The client\'s company')
@click.option('-e','--email',
              type=str,
              prompt=True,
              help='The client\'s email')
@click.option('-p','--position',
              type=str,
              prompt=True,
              help='The client\'s position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client

    Args:
        ctx (Context): click's context
        name (str): client's name
        company (str): client's company
        email (str): client's email address
        position (str): client's position
    """
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])
    client_service.create_client(client)

    pass


@clients.command()
@click.pass_context
def list(ctx):
    """Lists all clients

    Args:
        ctx (Context): click's context
    """
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.list_clients()
    click.echo('ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION')
    click.echo('*'*50)
    for client in clients_list:
        click.echo(f'{client["uid"]}  |  {client["name"]}  |  {client["company"]}  |  {client["email"]}  |  {client["position"]}')

@clients.command()
@click.argument('uid',
                 type=str)
@click.pass_context
def update(ctx, uid):
    """Updates a client

    Args:
        ctx (Context): click's context
        uid (int): client's uid
    """
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()

    client = [client for client in client_list if client['uid'] == uid]
    
    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)
    else:
        click.echo('Client not found')


def _update_client_flow(client):
    click.echo('Leave empty if you don\'t want to to modify the value')
    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)

    return client


@clients.command()
@click.argument('uid',
                 type=str)
@click.pass_context
def delete(ctx,uid):
    """Deletes a client

    Args:
        ctx (Context): click's context
        uid (int): client's uid
    """
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()

    client = [client for client in client_list if client['uid'] == uid]
    
    if client:
        client_service.delete_client(uid)
    else:
        click.echo('Client not found')

all = clients