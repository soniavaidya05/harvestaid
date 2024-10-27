import json
from User import User

# Creating Users and Listings
# Creating Users and Listings
maira = User("maira", "maira123", "maira@gmail.com")
maira.new_listing("Product_Category", "Corn Seeds", "Mumbai", "Selling 1 bag of Corn Seeds!", "/static/images/product.jpg")
maira.new_listing("Product_Category", "Wheat Seeds", "Chennai", "High-quality wheat seeds for optimal yield.", "/static/images/product.jpg")
maira.new_listing("Product_Category", "Tomato Seeds", "Jaipur", "Fresh and organic tomato seeds available!", "/static/images/product.jpg")
maira.new_listing("Product_Category", "Carrot Seeds", "Ahmedabad", "Nutritious carrot seeds, perfect for home gardens.", "/static/images/product.jpg")
maira.new_listing("Product_Category", "Cucumber Seeds", "Hyderabad", "Crisp cucumber seeds for summer harvest.", "/static/images/product.jpg")
maira.new_listing("Product_Category", "Lettuce Seeds", "Pune", "Get your fresh lettuce seeds for a healthy salad!", "/static/images/product.jpg")
maira.new_listing("Product_Category", "Bell Pepper Seeds", "Bangalore", "Vibrant bell pepper seeds for your garden.", "/static/images/product.jpg")
maira.new_listing("Product_Category", "Pumpkin Seeds", "Nagpur", "Large pumpkin seeds for fall harvest.", "/static/images/product.jpg")
maira.new_listing("Product_Category", "Radish Seeds", "Surat", "Fast-growing radish seeds, ready to harvest in weeks.", "/static/images/product.jpg")
maira.new_listing("Product_Category", "Herb Seeds", "Bhopal", "Variety of herb seeds for flavor in your dishes!", "/static/images/product.jpg")

amin = User("amin", "amin123", "amin@gmail.com")
amin.new_listing("Labour_Category", "Farm Hand", "Karachi", "Dedicated farm hand available for drought-resistant farming.", "/static/images/labour.jpg")
amin.new_listing("Labour_Category", "Livestock Caretaker", "Lahore", "Experienced livestock caretaker for challenging conditions.", "/static/images/labour.jpg")
amin.new_listing("Labour_Category", "Irrigation Technician", "Multan", "Skilled technician for water-efficient irrigation systems.", "/static/images/labour.jpg")
amin.new_listing("Labour_Category", "Crop Scout", "Islamabad", "Available for field inspections, pest management, soil monitoring.", "/static/images/labour.jpg")
amin.new_listing("Labour_Category", "Greenhouse Assistant", "Quetta", "Greenhouse assistant for drought-tolerant plants and flowers.", "/static/images/labour.jpg")
amin.new_listing("Labour_Category", "Farm Equipment Operator", "Faisalabad", "Certified operator focusing on drought mitigation.", "/static/images/labour.jpg")
amin.new_listing("Labour_Category", "Organic Farm Worker", "Peshawar", "Organic farm worker available for hands-on tasks in drought areas.", "/static/images/labour.jpg")
amin.new_listing("Labour_Category", "Dairy Farm Assistant", "Hyderabad (Pakistan)", "Dairy farm assistant implementing water conservation practices.", "/static/images/labour.jpg")
amin.new_listing("Labour_Category", "Harvesting Team Member", "Rawalpindi", "Experienced in sustainable picking practices during drought.", "/static/images/labour.jpg")
amin.new_listing("Labour_Category", "Poultry Farm Worker", "Sialkot", "Poultry worker managing drought-related challenges.", "/static/images/labour.jpg")

nathan = User("nathan", "nathan123", "nathan@gmail.com")
nathan.new_listing("Service_Category", "Irrigation", "Casablanca", "Licensed in setting up irrigation systems.", "/static/images/service.jpg")
nathan.new_listing("Service_Category", "Agronomy Consultant", "Marrakech", "Crop management advice and soil health assessments.", "/static/images/service.jpg")
nathan.new_listing("Service_Category", "Farm Management Advisor", "Agadir", "Farm management advisor for strategic planning.", "/static/images/service.jpg")
nathan.new_listing("Service_Category", "Livestock Nutritionist", "Fes", "Livestock nutrition specialist for health optimization.", "/static/images/service.jpg")
nathan.new_listing("Service_Category", "Pest Control Specialist", "Tangier", "Licensed pest control for sustainable crop protection.", "/static/images/service.jpg")
nathan.new_listing("Service_Category", "Veterinarian", "Rabat", "Veterinarian providing health care for farm animals.", "/static/images/service.jpg")
nathan.new_listing("Service_Category", "Soil Scientist", "Ouarzazate", "Conducting soil tests and recommending crop amendments.", "/static/images/service.jpg")
nathan.new_listing("Service_Category", "Agricultural Engineer", "Essaouira", "Engineer focused on designing efficient farm structures.", "/static/images/service.jpg")
nathan.new_listing("Service_Category", "Farm Safety Consultant", "El Jadida", "Providing assessments and training for farm safety.", "/static/images/service.jpg")
nathan.new_listing("Service_Category", "Organic Certification Specialist", "Meknes", "Specialist in organic certification for sustainable farming.", "/static/images/service.jpg")

sonia = User("sonia", "sonia123", "sonia@gmail.com")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Karachi", "6 hours", "/static/images/transportation.jpg")
sonia.new_listing("Transportation_Category", "Donkey for loan", "Marrakech", "5 hours", "/static/images/transportation.jpg")
sonia.new_listing("Transportation_Category", "Car for rent", "Hyderabad (India)", "8 hours", "/static/images/transportation.jpg")
sonia.new_listing("Transportation_Category", "Truck for Rent", "Ahmedabad", "7 hours", "/static/images/transportation.jpg")
sonia.new_listing("Transportation_Category", "Van for Rent", "Jaipur", "9 hours", "/static/images/transportation.jpg")

kevin = User("kevin", "kevin123", "kevin@gmail.com")
kevin.new_listing("Livestock_Category", "Chickens", "Karachi", "5 available", "/static/images/livestock.jpg")
kevin.new_listing("Livestock_Category", "Cattle", "Marrakech", "5 available", "/static/images/livestock.jpg")
kevin.new_listing("Livestock_Category", "Sheep", "Tangier", "8 available", "/static/images/livestock.jpg")
kevin.new_listing("Livestock_Category", "Goats", "Fes", "4 available", "/static/images/livestock.jpg")
kevin.new_listing("Livestock_Category", "Pigs", "Multan", "6 available", "/static/images/livestock.jpg")


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
            "description": listing.description,
            "image_url": listing.image_url
        }
        data.append(entry)

with open('listingdatabase.json', 'w') as f:
    json.dump(data, f, indent=4)
