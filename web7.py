# doing necessary imports

from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)  # initialising the flask app with the name 'app'

@app.route('/',methods=['POST','GET']) # route with allowed methods as POST and GET
def index():
    if request.method == 'POST':
        searchString = request.form['content'].replace(" ","") # obtaining the search string entered in the form
        try:
            url = "https://www.holidify.com/places/" + searchString
            content = requests.get(url)
            soup = BeautifulSoup(content.text, "html.parser")
            link = 'https://www.holidify.com' + soup.find('a', attrs={'class': 'num-reviews'})['href']
            content = requests.get(link)
            soup = BeautifulSoup(content.text, "html.parser")
            commentboxes = soup.find_all('div', attrs={'class': 'col-12 mb-30'})
            commentboxes = commentboxes[:-1]

            reviews = [] # initializing an empty list for reviews
            #  iterating over the comment section to get the details of customer and their comments
            for commentbox in commentboxes:
                try:
                    name = commentbox.find('b',attrs={'class':'mr-2'}).text

                except:
                    name = 'No Name'

                try:
                    review = commentbox.find('div',attrs={'class':'readMoreSmall'}).text

                except:
                    review = 'No Review'

                #fw.write(searchString+","+name.replace(",", ":")+","+rating + "," + commentHead.replace(",", ":") + "," + custComment.replace(",", ":") + "\n")
                mydict = {"Place": searchString, "Name": name, "Review": review} # saving that detail to a dictionary
                #x = table.insert_one(mydict) #insertig the dictionary containing the review comments to the collection
                reviews.append(mydict) #  appending the comments to the review list
            return render_template('results.html', reviews=reviews) # showing the review to the user
        except:
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(port=8000,debug=True) # running the app on the local machine on port 8000