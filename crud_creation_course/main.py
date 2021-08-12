import sys
import csv
import os

CLIENT_TABLE = 'C:/Users/JuanseDesktop/Documents/Courses/platzi_python_django/crud_creation_course/clients.csv'
CLIENT_SCHEMA = ['uid','name','company','email','position']
clients = []

def _initialize_clients():
    #TODO: create if it doesn't exists
    with open(CLIENT_TABLE, 'r') as file:
        reader = csv.DictReader(file, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_csv(clients):
    tmp_table_name = f'{CLIENT_TABLE}.tmp'
    with open(tmp_table_name, 'w') as f:
        writer = csv.DictWriter(f, CLIENT_SCHEMA)
        writer.writerows(clients)
        
        os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name,CLIENT_TABLE)


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
    print(f'{CLIENT_SCHEMA[0]} | {CLIENT_SCHEMA[1]} | {CLIENT_SCHEMA[2]} | {CLIENT_SCHEMA[3]} | {CLIENT_SCHEMA[4]}')
    print('*'*50)
    for idx, client in enumerate(clients):
        print(f'{idx} | {client["name"]} | {client["company"]} | {client["email"]} | {client["position"]}')


def _get_property(property,updated = False):
    client_property = None
    while client_property is None:
        if updated:
             client_property = input(f'What is the updated client {property}? ')
        else:
            client_property = input(f'What is the client {property}? ')
        if client_property == 'exit':
            client_property = None
            break
        if property == 'uid':
            client_property = int(client_property)

    if client_property is None:
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
    _initialize_clients()
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
    elif command == 'L':
        list_clients()
    elif command == 'D':
        index = _get_property('uid')
        delete_client(index)
    elif command == 'U':
        client = {
            'uid' : _get_property('uid'),
            'name': _get_property('name',True),
            'company': _get_property('company',True),
            'email': _get_property('email',True),
            'position': _get_property('position',True)
        }
        update_client(client)
    elif command == 'S':
        index = _get_property('uid')
        found = search_client(index)
        if found:
            print('The client is in the client\'s list')
        else:
            print(f'The client with uid {index} is not in our client\'s list')
    else:
        print('Invalid command')
    _save_clients_to_csv(clients)