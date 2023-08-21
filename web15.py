import requests
from bs4 import BeautifulSoup
import csv

# Make a GET request to the website
url = "https://www.holidify.com/country/india/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the HTML elements that contain city names and descriptions
city_elements = soup.find_all('div', {'class': 'card-body'})

# Extract the text content of each city element
city_info = []
for elem in city_elements:
    city_name = elem.find('h2', {'class': 'card-heading'})
    if city_name:
        city_name = city_name.text.strip()
    else:
        city_name = 'N/A'

    city_desc = elem.find('div', {'class': 'card-text'})
    if city_desc:
        city_desc = city_desc.text.strip()
    else:
        city_desc = 'N/A'

    city_info.append({'Name': city_name, 'Description': city_desc})

# Write the city names and descriptions to a CSV file
with open('cities.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Description'])
    writer.writeheader()
    writer.writerows(city_info)

# Print a message indicating the number of cities extracted and the name of the CSV file
print(f'Successfully extracted {len(city_info)} cities and saved them in "cities.csv" file.')
