
class Category: 
    """Categorizing the listings """
    listings: list

    def __init__(self, listings: list) -> None:
        self.listings = listings

    def add(self, listing) -> None:
        self.listings.append(listing) 


class Product(Category):
    """All the listings that hold products"""
    listings: list

class Labour(Category):
    """All the listings that advertise labour"""
    listings: list

class Services(Category):
    """All the listings that advertise professional services such as drought dugouts and 
    implementing irrigation systems
    """
    listings: list

class Transportation(Category):
    """All the listings that advertise transportation such as cars, trucks,etc. """
    listings: list

class Lifestock(Category):
    """All the listings that advertise sale of lifestock and related materials such as 
     feed, supplies, etc. """
    listings: list