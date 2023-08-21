import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://www.holidify.com/country/india/places-to-visit.html"
response = requests.get(url)

# Parse HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find the container with the top destinations
top_destinations = soup.find("div", {"class": "top-destinations"})
if top_destinations is not None:
    # Find all the destination boxes and extract information
    destination_boxes = top_destinations.find_all("div", {"class": "destination-box"})
    for box in destination_boxes:
        # Extract name and URL of destination
        name = box.find("div", {"class": "destination-name"}).text
        url = box.find("a", {"class": "destination-link"})["href"]
        print(name, url)
else:
    print("Could not find top destinations container.")

