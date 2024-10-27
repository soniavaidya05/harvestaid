import json
from User import User

# Creating Users and Listings
maira = User("maira", "maira123", "maira@gmail.com")
maira.new_listing("Product_Category", "Corn Seeds", "Mumbai", "Selling 1 bag of Corn Seeds!")
maira.new_listing("Product_Category", "Wheat Seeds", "Chennai", "High-quality wheat seeds for optimal yield.")
maira.new_listing("Product_Category", "Tomato Seeds", "Jaipur", "Fresh and organic tomato seeds available!")
maira.new_listing("Product_Category", "Carrot Seeds", "Ahmedabad", "Nutritious carrot seeds, perfect for home gardens.")
maira.new_listing("Product_Category", "Cucumber Seeds", "Hyderabad", "Crisp cucumber seeds for summer harvest.")
maira.new_listing("Product_Category", "Lettuce Seeds", "Pune", "Get your fresh lettuce seeds for a healthy salad!")
maira.new_listing("Product_Category", "Bell Pepper Seeds", "Bangalore", "Vibrant bell pepper seeds for your garden.")
maira.new_listing("Product_Category", "Pumpkin Seeds", "Nagpur", "Large pumpkin seeds for fall harvest.")
maira.new_listing("Product_Category", "Radish Seeds", "Surat", "Fast-growing radish seeds, ready to harvest in weeks.")
maira.new_listing("Product_Category", "Herb Seeds", "Bhopal", "Variety of herb seeds for flavor in your dishes!")

amin = User("amin", "amin123", "amin@gmail.com")
amin.new_listing("Labour_Category", "Farm Hand", "Karachi", "Dedicated farm hand available for drought-resistant farming.")
amin.new_listing("Labour_Category", "Livestock Caretaker", "Lahore", "Experienced livestock caretaker for challenging conditions.")
amin.new_listing("Labour_Category", "Irrigation Technician", "Multan", "Skilled technician for water-efficient irrigation systems.")
amin.new_listing("Labour_Category", "Crop Scout", "Islamabad", "Available for field inspections, pest management, soil monitoring.")
amin.new_listing("Labour_Category", "Greenhouse Assistant", "Quetta", "Greenhouse assistant for drought-tolerant plants and flowers.")
amin.new_listing("Labour_Category", "Farm Equipment Operator", "Faisalabad", "Certified operator focusing on drought mitigation.")
amin.new_listing("Labour_Category", "Organic Farm Worker", "Peshawar", "Organic farm worker available for hands-on tasks in drought areas.")
amin.new_listing("Labour_Category", "Dairy Farm Assistant", "Hyderabad (Pakistan)", "Dairy farm assistant implementing water conservation practices.")
amin.new_listing("Labour_Category", "Harvesting Team Member", "Rawalpindi", "Experienced in sustainable picking practices during drought.")
amin.new_listing("Labour_Category", "Poultry Farm Worker", "Sialkot", "Poultry worker managing drought-related challenges.")

nathan = User("nathan", "nathan123", "nathan@gmail.com")
nathan.new_listing("Service_Category", "Irrigation", "Casablanca", "Licensed in setting up irrigation systems.")
nathan.new_listing("Service_Category", "Agronomy Consultant", "Marrakech", "Crop management advice and soil health assessments.")
nathan.new_listing("Service_Category", "Farm Management Advisor", "Agadir", "Farm management advisor for strategic planning.")
nathan.new_listing("Service_Category", "Livestock Nutritionist", "Fes", "Livestock nutrition specialist for health optimization.")
nathan.new_listing("Service_Category", "Pest Control Specialist", "Tangier", "Licensed pest control for sustainable crop protection.")
nathan.new_listing("Service_Category", "Veterinarian", "Rabat", "Veterinarian providing health care for farm animals.")
nathan.new_listing("Service_Category", "Soil Scientist", "Ouarzazate", "Conducting soil tests and recommending crop amendments.")
nathan.new_listing("Service_Category", "Agricultural Engineer", "Essaouira", "Engineer focused on designing efficient farm structures.")
nathan.new_listing("Service_Category", "Farm Safety Consultant", "El Jadida", "Providing assessments and training for farm safety.")
nathan.new_listing("Service_Category", "Organic Certification Specialist", "Meknes", "Specialist in organic certification for sustainable farming.")

sonia = User("sonia", "sonia123", "sonia@gmail.com")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Karachi", "Truck License")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Marrakech", "Truck License")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Hyderabad (India)", "Truck License")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Ahmedabad", "Truck License")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Jaipur", "Truck License")

kevin = User("kevin", "kevin123", "kevin@gmail.com")
kevin.new_listing("Livestock_Category", "Chickens", "Karachi", "5 available")
kevin.new_listing("Livestock_Category", "Cattle", "Marrakech", "5 available")
kevin.new_listing("Livestock_Category", "Sheep", "Tangier", "8 available")
kevin.new_listing("Livestock_Category", "Goats", "Fes", "4 available")
kevin.new_listing("Livestock_Category", "Pigs", "Multan", "6 available")

# List of users and their listings
users = [maira, amin, sonia, nathan, kevin]

# Writing data to JSON
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
