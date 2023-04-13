# This module is used to handling mapping and recommendations for recommending restaurants and dishes to users based
# on their preferences, friends and communities.
from categories.models import Category
from restaurant.models import Restaurant
import random

def loadRestaurantIntoCategories():
    categories = ["Pizza", "Burger", "BBQ", "Sushi", "Vegan", "Desserts"]
    for category in categories:
        if not Category.objects.filter(name=category).exists():
            db_category:Category = Category.objects.create(name=category)
            randomlist = []
            for i in range(0,15):
                n = random.randint(1,30)
                randomlist.append(n)
            
            restaurants = Restaurant.objects.filter(id__in=randomlist)
            db_category.restaurants.add(*restaurants)
            db_category.save()
    print("Done!")
            

loadRestaurantIntoCategories()
                        
