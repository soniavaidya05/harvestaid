

class Category: 
    """Categorizing the listings """
    listings: list[Listing]
    def __init__(self) -> None:
        self.listings = listings

    def add(listing: Listing) -> None:
        listings.append(listing) 


class Product(Category):
    """All the listings that hold products"""
    listings: list[Listing]


class Labour(Category):
    """All the listings that advertise labour"""
    listings: list[Listing]

class Services(Category):
    """All the listings that advertise professional services such as drought dugouts and 
    implementing irrigation systems
    """
    listings: list[Listing]

class Transportation(Category):
    """All the listings that advertise transportation such as cars, trucks,etc. """
    listings: list[Listing]

class Lifestock(Category):
    """All the listings that advertise sale of lifestock and related materials such as 
     feed, supplies, etc. """
    listings: list[Listing]