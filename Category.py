class Category:
    """Categorizing the listings"""
    listings: list

    def __init__(self) -> None:
        self.listings = []

    def add(self, listing) -> None:
        self.listings.append(listing)

    def __str__(self) -> str:
        return "Category"  # Generic name for the base class


class Product(Category):
    """All the listings that hold products"""

    def __str__(self) -> str:
        return "Product"


class Labour(Category):
    """All the listings that advertise labour"""

    def __str__(self) -> str:
        return "Labour"


class Services(Category):
    """All the listings that advertise professional services such as drought dugouts and 
    implementing irrigation systems
    """

    def __str__(self) -> str:
        return "Services"


class Transportation(Category):
    """All the listings that advertise transportation such as cars, trucks, etc."""

    def __str__(self) -> str:
        return "Transportation"


class Livestock(Category):
    """All the listings that advertise sale of livestock and related materials such as 
     feed, supplies, etc.
    """

    def __str__(self) -> str:
        return "Livestock"
