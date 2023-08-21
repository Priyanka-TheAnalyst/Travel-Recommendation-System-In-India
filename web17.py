import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://www.holidify.com/places/wayanad/")

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, "html.parser")

# Find the section containing the ratings
rating_section = soup.find("div", {"class": "rating-section"})

# Extract the ratings
ratings = {}
if rating_section is not None:
    for rating in rating_section.find_all("div", {"class": "rating"}):
        category = rating.find("div", {"class": "category"}).text.strip()
        value = rating.find("div", {"class": "value"}).text.strip()
        ratings[category] = value

# Print the ratings
print(ratings)
