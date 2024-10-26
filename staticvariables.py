import Category
from Category import Product
from Category import Labour
from Category import Services
from Category import Transportation
from Category import Lifestock

Product_Category = Product()
Labour_Category = Labour()
Service_Category = Services()
Transportation_Category = Transportation()
Lifestock_Category = Lifestock()

map = {"Product_Category" : Product_Category,"Labour_Category": Labour_Category,
                "Service_Category": Service_Category, "Transportation_Category": Transportation_Category, 
                "Lifestock_Category": Lifestock_Category  }

def choose_category(self, name: str) -> Category:
        return map(name)