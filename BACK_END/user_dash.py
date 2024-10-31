from User import User

clients_logins = {}
clients = {}

def signup_func(u, e, p) -> bool:
    if u not in clients_logins: 
        clients_logins[u] = p
        clients[u] = (User(u, p, e))
        return True
    else: 
        return False


def login_func(u, p) -> bool: 
    if clients_logins[u] == p: 
            # return clients[username]
            return True
    else: 
        return False
