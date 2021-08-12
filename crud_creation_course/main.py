import sys


clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer'
    },
    {
        'name':'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer'
    }

]


def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def update_client(client):
    global clients
    index = int(client['uid'])
    if 0 <= index and index <= len(clients)-1:
        clients[index] = client
    else:
        print('Client is not in client\'s list')


def search_client(index):
    global clients
    if 0 <= index and index <= len(clients)-1:
        return clients[index]['name']



def delete_client(index):
    global clients

    if 0 <= index and index <= len(clients)-1:
        clients.pop(index)
    else:
        print('Client is not in client\'s list')



def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print(f'{idx} | {client["name"]} | {client["company"]} | {client["email"]} | {client["position"]}')


def _get_property(property,updated = False):
    client_property = None
    while not client_property:
        if updated:
             client_property = input(f'What is the updated client {property}? ')
        else:
            client_property = input(f'What is the client {property}? ')
        if property == 'uid':
            client_property = int(client_property)
        if client_property == 'exit':
            client_property = None
            break

    if not client_property:
            sys.exit()

    return client_property

def _print_welcome():
    print('WELCOME TO PLATZI SALES')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')



if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_property('name'),
            'company': _get_property('company'),
            'email': _get_property('email'),
            'position': _get_property('position')
        }
        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'D':
        index = _get_property('uid')
        delete_client(index)
        list_clients()
    elif command == 'U':
        client = {
            'uid' : _get_property('uid'),
            'name': _get_property('name',True),
            'company': _get_property('company',True),
            'email': _get_property('email',True),
            'position': _get_property('position',True)
        }
        update_client(client)
        list_clients()
    elif command == 'S':
        index = _get_property('uid')
        found = search_client(index)
        if found:
            print('The client is in the client\'s list')
        else:
            print(f'The client with uid {index} is not in our client\'s list')
    else:
        print('Invalid command')