import Category as Category
from Category import Product
from Category import Labour
from Category import Services
from Category import Transportation
from Category import Livestock

Product_Category = Product()
Labour_Category = Labour()
Service_Category = Services()
Transportation_Category = Transportation()
Livestock_Category = Livestock()

map = {"Product_Category" : Product_Category,"Labour_Category": Labour_Category,
                "Service_Category": Service_Category, "Transportation_Category": Transportation_Category, 
                "Livestock_Category": Livestock_Category  }

def choose_category(name: str) -> Category:
        return map[name]

