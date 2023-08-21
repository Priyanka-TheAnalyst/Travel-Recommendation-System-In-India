import requests
from bs4 import BeautifulSoup
import pandas as pd
pages = []
for i in range(1, 10, 1):
    url = "https://www.holidify.com/country/india/places-to-visit.html" + str(i) + '.html'
    pages.append(url)
    for item in pages:
        page = requests.get(item)
        soup = BeautifulSoup(page.text, 'html.parser')
        Place = list(soup.find(class_="col-md-10 col-xs-10 nopadding"))[1].get_text()
        City = list(soup.find_all(class_="smallerText"))[1].get_text()
        State = list(soup.find_all(class_="smallerText"))[2].get_text()
        Country = list(soup.find_all(class_="smallerText"))[3].get_text()
        About = list(soup.find_all(class_="biggerTextOverview"))[0].get_text()
        more_About = list(soup.find_all(class_="objHeading smallerText"))[0].get_text()
        Weather = soup.find(class_="currentWeather").get_text()
        demo = pd.DataFrame({ "Place": Place, "City": City, "State": State, "Country": Country, "About": About,"More About Places": more_About}, index=[0])
        demo.to_csv('demo.csv', index=False, encoding='utf-8')