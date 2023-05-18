import requests
from bs4 import BeautifulSoup as bs

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

city = input("Enter the city: ")
checkin_date = input("Enter the check-in date (YYYY-MM-DD): ")
checkout_date = input("Enter the check-out date (YYYY-MM-DD): ")

search_params = {
    "ss": city,
    "ssne": city,
    "ssne_untouched": city,
    "checkin": checkin_date,
    "checkout": checkout_date,
    "group_adults": 1,
    "no_rooms": 1,
    "group_children": 0
}

url = "https://www.booking.com/searchresults.html"
req = requests.get(url, params=search_params, headers=headers)
soup = bs(req.text, 'html.parser')

for i in range(0, 5):
    name = soup.find_all("div", {"class": "fcab3ed991 a23c043802"})
    print(name[i].text)

    rating = soup.find_all("div", {"class": "b5cd09854e d10a6220b4"})
    print(rating[i].text)

    price = soup.find_all("span", {"class": "fcab3ed991 fbd1d3018c e729ed5ab6"})
    print(price[i].text, "\n")