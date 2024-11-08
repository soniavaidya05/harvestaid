from listing import Listing
import staticvariables as staticvariables
import json 

class User: 
    username: str
    password: str
    listings: list
    needs: list 
    email: str
    def __init__(self, username: str, password: str, email: str, listings=None, needs=None) -> None:
        self.username = username
        self.password = password
        self.email = email
        # Use the provided listings or default to an empty list
        self.listings = listings if listings is not None else []
        # Use the provided needs or default to an empty list
        self.needs = needs if needs is not None else []

    def new_listing(self, category:str, product_name: str, location: str, description: str, image_url: str) -> None: 
        listing = Listing(self.username, category, product_name, location, description, image_url)
        self.listings.append(listing)

        # Convert the listing to dictionary
        staticvariables.map[category].add(listing)

        with open('all_users.json', 'r+') as file:
            all_users = json.load(file)
        

        # Update the user's listings
        all_users[self.username] = all_users.get(self.username, {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "listings": [],
            "needs": []
        })
        
        all_users[self.username]["listings"] = [listing.to_dict() for listing in self.listings if isinstance(listing, Listing)]

        # Write the updated data back to the JSON file
        with open("all_users.json", "w") as f:
            json.dump(all_users, f, indent=4)

        with open('listingdatabase.json', 'r+') as file:
            products = json.load(file)
        
            # Convert the new listing to a dictionary and append it to the global product list
            products.append(listing.to_dict())
            
            # Save the updated list back to the file
            file.seek(0)  # Move the cursor back to the beginning of the file to overwrite
            json.dump(products, file, indent=4)
            file.truncate()

    def new_need(self, need:str)-> None: 
        self.needs.append(need)
    
    def to_dict(self):
        # Convert user object to dictionary, ensuring all attributes are serializable
        return {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "listings": [listing.to_dict() for listing in self.listings],  # Serialize listings
            "needs": self.needs
        }
