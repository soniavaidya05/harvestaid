from listing import Listing
import staticvariables as staticvariables

class User: 
    username: str
    password: str
    listings: list
    needs: list 
    email: str
    def __init__(self, username:str, password: str, email: str) -> None:
        self.username = username
        self.password = password
        self.listings = []
        self.email = email
        self.needs = []
    
    def new_listing(self, category:str, product_name: str, location: str, description: str, image_url: str) -> None: 
        listing = Listing(self.username, category, product_name, location, description, image_url)
        self.listings.append(listing)
        staticvariables.map[category].add(listing)

    def new_need(self, need:str)-> None: 
        self.needs.append(need)