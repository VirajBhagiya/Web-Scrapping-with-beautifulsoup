import requests  
from bs4 import BeautifulSoup as bs

url = ["https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen", "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen", "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen", "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen", "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen", "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen", "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen", "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp0Y1RjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen", "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"]


print("Fields: Top Stories, India, World, Business, Technology, Entertainment, Sports, Science, Health")
field = input("Select the field: ")

if field == "Top Stories":
    req = requests.get(url[0])
    soup = bs(req.text, 'html.parser')
    TopStories = soup.find_all("h4", {"class": "gPFEn"})
    for line in TopStories[:10]:
        print(line.text,"\n")
elif field == "India":
    req = requests.get(url[1])
    soup = bs(req.text, 'html.parser')
    India = soup.find_all("h4", {"class": "gPFEn"})
    for line in India[:10]:
        print(line.text,"\n")
elif field == "World":
    req = requests.get(url[2])
    soup = bs(req.text, 'html.parser')
    World = soup.find_all("h4", {"class": "gPFEn"})
    for line in World[:10]:
        print(line.text,"\n")
elif field == "Business":
    req = requests.get(url[3])
    soup = bs(req.text, 'html.parser')
    Business = soup.find_all("h4", {"class": "gPFEn"})
    for line in Business[:10]:
        print(line.text,"\n")
elif field == "Technology":
    req = requests.get(url[4])
    soup = bs(req.text, 'html.parser')
    Technology = soup.find_all("h4", {"class": "gPFEn"})
    for line in Technology[:10]:
        print(line.text,"\n")
elif field == "Entertainment":
    req = requests.get(url[5])
    soup = bs(req.text, 'html.parser')
    Entertainment = soup.find_all("h4", {"class": "gPFEn"})
    for line in Entertainment[:10]:
        print(line.text,"\n")
elif field == "Sports":
    req = requests.get(url[6])
    soup = bs(req.text, 'html.parser')
    Sports = soup.find_all("h4", {"class": "gPFEn"})
    for line in Sports[:10]:
        print(line.text,"\n")
elif field == "Science":
    req = requests.get(url[7])
    soup = bs(req.text, 'html.parser')
    Science = soup.find_all("h4", {"class": "gPFEn"})
    for line in Science[:10]:
        print(line.text,"\n")
elif field == "Health":
    req = requests.get(url[8])
    soup = bs(req.text, 'html.parser')
    Health = soup.find_all("h4", {"class": "gPFEn"})
    for line in Health[:10]:
        print(line.text,"\n")
else:
    print("Invalid Input")