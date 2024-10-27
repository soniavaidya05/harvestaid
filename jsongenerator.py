import json
from staticvariables import Product_Category
from User import User

maira = User("maira", "maira123", "maira@gmail.com")
maira.new_listing("Product_Category", "Corn Seeds", "Toronto", "Selling 1 bag of Corn Seeds!")
maira.new_listing("Product_Category", "Wheat Seeds", "Ottawa", "High-quality wheat seeds for optimal yield.")
maira.new_listing("Product_Category", "Tomato Seeds", "Mississauga", "Fresh and organic tomato seeds available!")
maira.new_listing("Product_Category", "Carrot Seeds", "Brampton", "Nutritious carrot seeds, perfect for home gardens.")
maira.new_listing("Product_Category", "Cucumber Seeds", "Hamilton", "Crisp cucumber seeds for summer harvest.")
maira.new_listing("Product_Category", "Lettuce Seeds", "London", "Get your fresh lettuce seeds for a healthy salad!")
maira.new_listing("Product_Category", "Bell Pepper Seeds", "Markham", "Vibrant bell pepper seeds for your garden.")
maira.new_listing("Product_Category", "Pumpkin Seeds", "Kitchener", "Large pumpkin seeds for fall harvest.")
maira.new_listing("Product_Category", "Radish Seeds", "Windsor", "Fast-growing radish seeds, ready to harvest in weeks.")
maira.new_listing("Product_Category", "Herb Seeds", "Richmond Hill", "Variety of herb seeds for flavor in your dishes!")

amin = User("amin", "amin123", "amin@gmail.com")
amin.new_listing("Labour_Category", "Farm Hand", "Chatham-Kent", "Dedicated farm hand available for planting, harvesting, and general maintenance, experienced in drought-resistant farming techniques.")
amin.new_listing("Labour_Category", "Livestock Caretaker", "Chatham-Kent", "Experienced livestock caretaker available to manage feeding, grooming, and health monitoring of farm animals during challenging conditions.")
amin.new_listing("Labour_Category", "Irrigation Technician", "Chatham-Kent", "Skilled irrigation technician available to install and maintain water-efficient irrigation systems for drought-prone crops.")
amin.new_listing("Labour_Category", "Crop Scout", "Chatham-Kent", "Detail-oriented crop scout available for field inspections, pest management, and monitoring soil moisture levels.")
amin.new_listing("Labour_Category", "Greenhouse Assistant", "Chatham-Kent", "Enthusiastic greenhouse assistant available for planting, watering, and caring for drought-tolerant plants and flowers.")
amin.new_listing("Labour_Category", "Farm Equipment Operator", "Chatham-Kent", "Certified farm equipment operator available to drive tractors and operate machinery for efficient field work, focusing on drought mitigation.")
amin.new_listing("Labour_Category", "Organic Farm Worker", "Chatham-Kent", "Passionate organic farm worker available for hands-on tasks, including weeding, planting, and harvesting drought-resistant crops.")
amin.new_listing("Labour_Category", "Dairy Farm Assistant", "Chatham-Kent", "Reliable dairy farm assistant available for milking, feeding, and caring for dairy cattle, implementing water conservation practices.")
amin.new_listing("Labour_Category", "Harvesting Team Member", "Chatham-Kent", "Hardworking harvesting team member available for seasonal work, experienced in picking fruits and vegetables with a focus on sustainable practices.")
amin.new_listing("Labour_Category", "Poultry Farm Worker", "Chatham-Kent", "Dedicated poultry farm worker available for managing feeding, health checks, and egg collection, aware of drought-related challenges.")

nathan = User("nathan", "nathan123", "nathan@gmail.com")
nathan.new_listing("Service_Category", "Irrigation", "Chatham-Kent", "Licensed in setting up Irrigation Systems")
nathan.new_listing("Service_Category", "Agronomy Consultant", "Essex County", "Expert agronomy consultant providing crop management advice and soil health assessments.")
nathan.new_listing("Service_Category", "Farm Management Advisor", "Haldimand County", "Experienced farm management advisor offering strategic planning and operational efficiency solutions.")
nathan.new_listing("Service_Category", "Livestock Nutritionist", "Lambton County", "Certified livestock nutritionist specializing in feed formulation and animal health optimization.")
nathan.new_listing("Service_Category", "Pest Control Specialist", "Perth County", "Licensed pest control specialist providing organic and sustainable solutions for crop protection.")
nathan.new_listing("Service_Category", "Veterinarian", "Brant County", "Qualified veterinarian offering health care services for farm animals and livestock.")
nathan.new_listing("Service_Category", "Soil Scientist", "Grey County", "Professional soil scientist conducting soil tests and recommending amendments for optimal crop growth.")
nathan.new_listing("Service_Category", "Agricultural Engineer", "Norfolk County", "Skilled agricultural engineer focused on designing efficient farm structures and machinery.")
nathan.new_listing("Service_Category", "Farm Safety Consultant", "Dufferin County", "Certified farm safety consultant providing assessments and training to enhance farm safety practices.")
nathan.new_listing("Service_Category", "Organic Certification Specialist", "Wellington County", "Specialist in organic certification processes and compliance for sustainable farming practices.")

sonia = User("sonia", "sonia123", "sonia@gmail.com")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Chatham-Kent", "Truck License")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Windsor", "Truck License")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Sarnia", "Truck License")
sonia.new_listing("Transportation_Category", "Truck for Rent", "London", "Truck License")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Leamington", "Truck License")
sonia.new_listing("Transportation_Category", "Truck for Rent", "St. Thomas", "Truck License")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Essex", "Truck License")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Tilbury", "Truck License")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Blenheim", "Truck License")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Chatham", "Truck License")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Kingsville", "Truck License")

kevin = User("kevin", "kevin123", "kevin@gmail.com")
kevin.new_listing("Livestock_Category", "Chickens", "Tilbury", "5 available")
kevin.new_listing("Livestock_Category", "Cattle", "Tilbury", "5 available")
kevin.new_listing("Livestock_Category", "Sheep", "Tilbury", "8 available")
kevin.new_listing("Livestock_Category", "Goats", "Tilbury", "4 available")
kevin.new_listing("Livestock_Category", "Pigs", "Tilbury", "6 available")
kevin.new_listing("Livestock_Category", "Chickens", "Tilbury", "20 available")
kevin.new_listing("Livestock_Category", "Turkeys", "Tilbury", "10 available")
kevin.new_listing("Livestock_Category", "Ducks", "Tilbury", "15 available")
kevin.new_listing("Livestock_Category", "Donkeys", "Tilbury", "2 available")
kevin.new_listing("Livestock_Category", "Geese", "Tilbury", "5 available")
kevin.new_listing("Livestock_Category", "Quail", "Tilbury", "30 available")


users = [maira, amin, sonia, nathan, kevin]
# Write data to JSON file
data = []
for user in users:
    for listing in user.listings:
        entry = {
            "contact": user.email,
            "category": str(listing.category),
            "product name": listing.product_name,
            "location": listing.location,
            "description": listing.description
        }
        data.append(entry)

with open('listingdatabase.json', 'w') as f:
    json.dump(data, f, indent=4)
