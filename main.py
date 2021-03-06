import csv
import os

clients = []
CLIENTS_TABLE = ".clients.csv"
CLIENTS_SCHEMA = ["name","company","email","role"]

def initialize_clients():
    with open(CLIENTS_TABLE, mode="r")as f:
        reader = csv.DictReader(f,fieldnames=CLIENTS_SCHEMA)
        for row in reader:
            clients.append(row)

def save_clients_to_storage():
    temp_table = '{}.tmp'.format(CLIENTS_TABLE)
    with open(temp_table, mode="w") as f:
        writer = csv.DictWriter(f, fieldnames=CLIENTS_SCHEMA)
        writer.writerows(clients)

    os.remove(CLIENTS_TABLE)
    os.rename(temp_table, CLIENTS_TABLE)   
            
def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print(f"the client: {client} is already on the clients list\n")

def list_clients():
    global clients
    print("\nClients:")
    for i, client in enumerate(clients):
        print('{} - {} - {}'.format(i+1,client["name"],client["company"]))
    print("\n")
    
     

#uc --> updated client
#c --> client
def update_client(c,uc):
    global clients
    for i in range(0,len(clients)):
        if clients[i]["name"] == c:
            clients[i]["name"] = uc
            print(f'{c} was updated to {uc} \n')
            list_clients()
            return True
    return False

def delete_client(c):
    global clients
    for i in range(0,len(clients)):
        if clients[i]["name"] == c:
            del clients[i]
            print(f'{c} was deleted succesfully\n')
            list_clients()
            return True
    return False

def search_client(c):
    global clients
    for i in range(0,len(clients)):
        if clients[i]["name"] == c:
            return True
            break
    return False
    
   


def _get_client_field(x):
    field = None
    while not field:
        field = input('please type the {} of the client:'.format(x))
    return field

               
   
def welcome():
    print("WELCOME TO CADAVINCI SALES")
    print("*" * 50)
    print("What would you like to do?")
    print("[C]reate client")
    print("[R]ead clients")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch client")

def run():
    initialize_clients()
    welcome()

if __name__ == "__main__":
    run()

    command = input()
    command = command.upper()

    if command == "C":
        client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'role': _get_client_field('position'),
        }
        create_client(client)
        list_clients()

    elif command == "R":
        list_clients()

    elif command == "U":
        client_name = _get_client_field(1)
        updated_client = input("please type the new name of the client: ")
        if (not update_client(client_name, updated_client)):
            print(f'Sorry but there is no such client as {client_name} in the list.')
        
        

    elif command == "D":
        client_name = _get_client_field(1)
        if (not delete_client(client_name)):
            print(f'Sorry but there is no such client as {client_name} in the list.')
    
    elif command == "S":
        client_name = _get_client_field(1)
        if (search_client(client_name)):
                print(f'{client_name} is in the list of clients')
        else:
            print(f'Sorry but there is no such client as {client_name} in the list.')
    
    else:
        print(f'Sorry but you chose an invalid option')
    
    save_clients_to_storage()