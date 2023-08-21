import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://www.holidify.com/country/india/places-to-visit.html"
response = requests.get(url)

# Parse HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Print the HTML content
print(soup.prettify())
