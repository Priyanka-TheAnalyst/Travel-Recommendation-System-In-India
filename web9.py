import requests
from bs4 import BeautifulSoup

# Send a request to the webpage
url = "https://www.holidify.com/country/india/places-to-visit.html"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the desired information from the webpage
title = soup.title.string
paragraphs = [p.text for p in soup.find_all('p')]
links = [a['href'] if 'href' in a.attrs else '' for a in soup.find_all('a')]

# Print the extracted information
print('Title:', title)
print('Paragraphs:', paragraphs)
print('Links:', links)
