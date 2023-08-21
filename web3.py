import requests
import csv
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://www.holidify.com/"
response = requests.get(url)

# Parse HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find the elements that contain the information you want to extract
destinations = soup.find_all("div", {"class": "col-12 col-sm-6 col-md-4"})

# Extract the information from each element and save it to a CSV file
with open("holidify_destinations.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Destination", "State", "Country", "Best Time to Visit", "Famous For", "Ideal Duration"])
    
    for destination in destinations:
        name = destination.find("h3", {"class": "card-heading"}).text.strip()
        state = destination.find("span", {"class": "card-state"}).text.strip()
        country = destination.find("span", {"class": "card-country"}).text.strip()
        best_time = destination.find("div", {"class": "card-info-heading"}, string="Best Time to Visit").find_next_sibling("div").text.strip()
        famous_for = destination.find("div", {"class": "card-info-heading"}, string="Famous For").find_next_sibling("div").text.strip()
        duration = destination.find("div", {"class": "card-info-heading"}, string="Ideal Duration").find_next_sibling("div").text.strip()
        
        writer.writerow([name, state, country, best_time, famous_for, duration])
