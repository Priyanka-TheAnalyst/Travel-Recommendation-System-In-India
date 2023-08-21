import requests
from bs4 import BeautifulSoup
import csv

# Make a GET request to the website
url = 'https://www.holidify.com/country/india/'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the HTML elements that contain city names
city_elements = soup.find_all('h2', {'class': 'card-heading'})

# Extract the text content of each city element
city_names = [elem.text for elem in city_elements]

# Write the city names to a CSV file
with open('cities.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['City Name'])
    for city in city_names:
        writer.writerow([city])
        
# Print a message indicating the number of cities extracted and the name of the CSV file
print(f'Successfully extracted {len(city_names)} cities and saved them in "cities.csv" file.')
