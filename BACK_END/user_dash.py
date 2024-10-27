import User as User

clients_logins = {}
clients = {}

def signup(username, password) -> bool:
    if username not in clients_logins: 
        clients_logins[username] = password
        clients[username] = (User(username, password))
        return True
    else: 
        return False


def login(username, password) -> bool: 
    if clients_logins[username] == password: 
            # return clients[username]
            return True
    else: 
        return False
