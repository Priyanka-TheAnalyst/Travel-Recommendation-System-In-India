import requests
from bs4 import BeautifulSoup
import csv

# Send a request to the webpage
url = "https://www.holidify.com/packages/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the desired information from the webpage
title = soup.title.string
paragraphs = [p.text for p in soup.find_all('p')]
links = [a['href'] if 'href' in a.attrs else '' for a in soup.find_all('a')]

# Write the extracted information to a CSV file
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Paragraphs', 'Links'])
    for paragraph, link in zip(paragraphs, links):
        if paragraph and link:
            writer.writerow([title, paragraph, link])
