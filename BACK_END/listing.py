import Category as Category
import staticvariables as staticvariables
import json

class Listing:
    """This class is the listing class.
    - Category 
    - Product name 
    - Location 

    METHODS:
    - choose category str
    - choose product str 
    - choose location 

    """
    
    category: Category
    product_name: str
    location: str
    description: str
    username: str
    image_url: str

    def __init__(self, username: str, category: str, product_name: str, location: str, description: str, image_url:str):
        self.username = username
        self.category = staticvariables.choose_category(category)
        self.product_name = product_name 
        self.location = location
        self.description = description
        self.image_url= image_url.replace("\\", "/")

    
    def to_dict(self):
        # Convert Listing object to dictionary
        try:
            with open('all_users.json', 'r') as file:
                all_users = json.load(file)
        except json.JSONDecodeError:
            all_users = {}  
        return {
            "contact": all_users[self.username]["email"],
            "category": str(self.category),  # Convert category to string (name)
            "product name": self.product_name,
            "location": self.location,
            "description": self.description,
            "image_url": self.image_url
        }