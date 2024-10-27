import Category
import staticvariables

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
        self.image_url= image_url