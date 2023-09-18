import requests
from bs4 import BeautifulSoup
import random
import string

for i in range(2, 169):
    url = f"https://api.contactcars.com/gateway/vehicles/classifiedAdsSearch/search?pageIndex={i}"

    response = requests.get(url).json()


    for car in response["result"]["items"]:
        for img in car["album"]:
            length = random.randint(4, 10)
            rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            with open(f"./images/{rand_str}.jpg", "wb") as f:
                f.write(requests.get("https://contactcars.fra1.cdn.digitaloceanspaces.com/contactcars-production/Images/Small/"+img).content)


