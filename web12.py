import requests
from bs4 import BeautifulSoup
import csv

# Send a request to the webpage
url = "https://www.holidify.com/packages/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the desired information from the webpage
packages = soup.find_all('div', class_='package-card')
package_data = []
for package in packages:
    name = package.find('h3', class_='card-heading').text.strip()
    location = package.find('p', class_='card-location').text.strip()
    duration = package.find('span', class_='card-duration').text.strip()
    price = package.find('span', class_='card-price').text.strip()
    rating = package.find('div', class_='card-rating').text.strip()
    review_count = package.find('div', class_='card-reviews').text.strip()
    description = package.find('div', class_='card-description').text.strip()
    package_data.append({
        'Name': name,
        'Location': location,
        'Duration': duration,
        'Price': price,
        'Rating': rating,
        'Review Count': review_count,
        'Description': description
    })

# Write the extracted information to a CSV file
with open('packages.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Location', 'Duration', 'Price', 'Rating', 'Review Count', 'Description'])
    for data in package_data:
        writer.writerow([data['Name'], data['Location'], data['Duration'], data['Price'], data['Rating'], data['Review Count'], data['Description']])
