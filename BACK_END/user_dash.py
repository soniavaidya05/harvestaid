from User import User
import json
# clients_logins = {}
# clients = {}


# def login_func(u, p) -> bool: 
#     if clients_logins[u] == p: 
#             # return clients[username]
#             return True
#     else: 
#         return False

try:
    with open('client_logins.json', 'r') as file:
        client_logins = json.load(file)
except json.JSONDecodeError:
    client_logins = {}  


try:
    with open("all_users.json", "r") as file:
        all_users_data = json.load(file)
        all_users = {}
        for username, user_data in all_users_data.items():
            # Create User instance with required fields, and pass other attributes separately
            all_users[username] = User(
                username=user_data['username'],
                password=user_data['password'],
                email=user_data['email'],
                listings=user_data.get('listings', []),  # Default to empty list if not found
                needs=user_data.get('needs', [])         # Default to empty list if not found
            )
except json.JSONDecodeError:
    all_users = {}



@staticmethod
def save_users(user_dict):
    # Convert User objects into dictionaries for storage
    users_to_save = {username: user.__dict__ for username, user in user_dict.items()}
    with open("all_users.json", "w") as file:
        json.dump(users_to_save, file, indent=4)  # Serialize to JSON format


@staticmethod
def get_user_by_username(username):
    # Retrieve the User object stored in the all_users dictionary
    return all_users.get(username)  # Return the User instance directly

    

# try:
#     with open('clients.json', 'r') as file2:
#         clients = json.load(file2)
# except json.JSONDecodeError:
#     clients = {} 


def save_client_logins():
    with open('client_logins.json', 'w') as file:
        json.dump(client_logins, file)
    # with open('clients.json', 'w') as file2:
    #     json.dump(clients, file2)

def signup_func(username, email, password) -> bool:
    if username not in client_logins: 
        client_logins[username] = password
        all_users[username] = User(username, password, email)
        save_client_logins()
        save_users(all_users)
        print(f"User {username} created and saved.")
        return True
    else: 
        print(f"User {username} already exists.")
        return False

def login_func(u, p) -> bool:
    return client_logins.get(u) == p