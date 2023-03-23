# This package contains the following modules:
#   - Engine for collecting data from the www.themealdb.com/ api.
#   - Engine for collecting data from the https://tasty.p.rapidapi.com/ api.
#   - Engine for collecting data from the https://worldwide-restaurants.p.rapidapi.com api.
#   - Engine to load data collected from the API inot the restaurants, dishes and tags model
import requests
import shutil
import random
from django.core.files.uploadedfile import UploadedFile
from restaurant.models import Restaurant, Dish


def loadImageFromUrl(url:str, name:str):
    res = requests.get(url, stream = True)
    file_name = f"{name}.jpg"
    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')
                
    image = None
    try:
        image=UploadedFile(file=open(f"{name}.jpg", 'rb'))
        print('Image Successfully Downloaded and loaded: ')
    except Exception as e:
        print("Image not found")
        
    return image
        

def getRestaurantsFromWorldRestaurant():
    url = "https://worldwide-restaurants.p.rapidapi.com/search"

    payload = "language=en_US&limit=30&location_id=297704&currency=USD"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "3556fae311msha4eee6b27ec2b1fp10839bjsnd8fca4b389aa",
        "X-RapidAPI-Host": "worldwide-restaurants.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    
    data = response.json()["results"]["data"]
    print("Gotten the data....")
    for entry in data:
        print("--------------------------------")
        print(f"Getting the data for {entry['name']}...")
        
        name:str = entry["name"]
        latitude = entry["latitude"]
        longitude = entry["longitude"]
        address = entry["address"]
        ranking = entry["ranking"]
        rating = entry["rating"]
        price_level = entry["price_level"]
        computed_email = name.lower().replace(" ", "")+"@gmail.com"
        email = entry.get("email", computed_email)
        phone = entry["phone"]
        description = entry["description"]
        if entry["photo"]["images"]["medium"]["url"]:
            print("Getting the image...")
            image_url = entry["photo"]["images"]["medium"]["url"]
            image = loadImageFromUrl(image_url, name)
        
        if not Restaurant.objects.filter(name=name).exists():
            print("Creating new restaurant ", name)
            restaurant:Restaurant = Restaurant.objects.create(name=name, email=email, description=description, address=address, 
                                                   phone=phone, image=image, long=longitude, 
                                                   lat=latitude, rating=rating,
                                                   ranking=ranking, price_level=price_level)
            restaurant.save()
            print("Created restaurant: ", name)
            
    return "complete"


def getDataFromMealDB(id: int):
    response = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}")
    if response.status_code == 200:
        result = response.json()
        return result
    return None

def scrapeMealDB():
    results = []
    for i in range(52700, 53700):
        result = getDataFromMealDB(i)
        results.append(result)
    
    # add results that are not none to the output file
    outputs = [result for result in results if result["meals"]]
        
    return outputs


def loadDishesIntoDatabase():
    results = scrapeMealDB()
    restuarants = Restaurant.objects.all()
    num_restaurants = len(restuarants)
    for result in results:
        meals = result["meals"]
        for meal in meals:
            name = meal["strMeal"]
            image_url = meal["strMealThumb"]
            image = loadImageFromUrl(image_url, name)
            category = meal["strCategory"]
            price = (random.random() * 200) + 1
            restaurant_id = random.randint(1, num_restaurants)
            
            # create database object
            restaurant = Restaurant.objects.get(id=restaurant_id)
            dish = Dish.objects.create(name=name, price=price, image=image, restaurant=restaurant)
            dish.save()           
             
        
