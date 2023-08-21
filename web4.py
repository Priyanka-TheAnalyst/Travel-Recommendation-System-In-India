import csv
import requests
from bs4 import BeautifulSoup

# URL of the HTML page to scrape
url = 'https://example.com/table.html'

# Send a GET request to the URL and store the response
response = requests.get(url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element in the HTML
table = soup.find('table')

# Find all rows in the table
rows = table.find_all('tr')

# Create a new CSV file and write the rows to it
with open('output.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in rows:
        # Find all cells in the row
        cells = row.find_all('td')
        # Extract the text content of each cell and write it to the CSV
        writer.writerow([cell.get_text(strip=True) for cell in cells])
