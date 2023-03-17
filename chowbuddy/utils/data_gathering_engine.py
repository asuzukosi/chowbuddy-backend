# This package contains the following modules:
#   - Engine for collecting data from the www.themealdb.com/ api.
#   - Engine for collecting data from the https://tasty.p.rapidapi.com/ api.
#   - Engine for collecting data from the https://worldwide-restaurants.p.rapidapi.com api.
#   - Engine to load data collected from the API inot the restaurants, dishes and tags model
import requests
import shutil
from django.core.files.uploadedfile import UploadedFile
from restaurant.models import Restaurant

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
            res = requests.get(image_url, stream = True)
            print("Image retrieved")
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
        
        if not Restaurant.objects.filter(name=name).exists():
            print("Creating new restaurant ", name)
            restaurant:Restaurant = Restaurant.objects.create(name=name, email=email, description=description, address=address, 
                                                   phone=phone, image=image, long=longitude, 
                                                   lat=latitude, rating=rating,
                                                   ranking=ranking, price_level=price_level)
            restaurant.save()
            print("Created restaurant: ", name)
            
    return "complete"
