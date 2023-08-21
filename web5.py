import requests
import bs4 as bs
import time
import json

months = {'January', "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December", "Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"}

header = {
    "Content-Type": "application/javascript",
    "User-Agent": "Mozilla",
    "Host": "https://www.holidify.com/"
}
print("")
print("holidify")
print("")


fp=open("https://www.holidify.com/weekend-getaways/from-bangalore.html","r")
data=json.load(fp)
print(data)

payload = {"tg_id": "Karnataka",
           "tguide_type": "tguide_place",
           }

url = "https://www.holidify.com/hotels/"

'''list = ["kudremukh", "dubare", "gokarn", "mangalore", "belgaum", "k-gudi", "bellary", "udupi", "jog-falls", "raichur",
        "hampi", "bandipur", "channarayapatna", "siddapur", "hassan", "shravanabelagola", "nagarhole", "shimoga",
        "manipal", "bijapur", "chikmagalur", "chitradurga", "tumkur", "madikeri", "uttara-kannada", "halebid",
        "dharwad", "gulbarga", "hubli", "coorg", "gangavathi", "badami", "bidar", "ganeshgudi", "bangalore", "karwar",
        "mysore", "dharmasthala", "bhagamandala", "dandeli", "bheemeshwari", "nandi-hills", "belur"]

count = 0

for state in data.keys():
    for place in data[state].keys():
        data[state][place] = {}
        count += 1
'''

for state in data.keys():
    for place in data[state].keys():
        if len(place.split())>1:
            u=place.replace(" ","-")
            u=u.lower

            print(place)
            payload["tg_id"] = u
            ourrequest = requests.get(url=url, headers=header, params=payload).json()
            try:
                if (ourrequest["success"]):
                    print("success")

                    line = ourrequest["data"]["parent"]["notes"]["Best Season"]
                    line = line.split()

                    count = 0
                    for word in line:
                        try:
                            if word in months and line[count + 2] in months:
                                print( line[count] + " to " + line[count + 2])
                                data[state][place]["goibibo"] = line[count] + " to " + line[count + 2]
                                print("ok")

                        except Exception:
                            continue
                        count += 1
                    s = requests.Session()
                    s.keep_alive = False

                # data[place]["holidify"]=ourrequest["data"]["parent"]["notes"]["Best Season"]
            except Exception:

                continue
    print(data[state])

print(data)
with open("tourism_data_3.json", "w") as outfile:
    json.dump(data, outfile)

header["Content-Type"]="text/html"


website = ["tourismofindia" ]
host = ["www.tourism-of-india.com"]
url_list1 = ["https://www.holidify.com/"]
url_list2 = ["/"]
html_list = ["section"]
class1 = ["best_time"]



for i in range(len(website)):

    print("")
    print(website[i])
    print("")

    header["Host"] = host[i]
    for state in data.keys():
        for place in data[state].keys():


            if len(place.split())>1:

                u = place.replace(" ", "-")
                u=u.lower()



                print(place)
                url = url_list1[i] + u + url_list2[i]
                print(url)
                try:
                    try:
                        ourrequest = requests.get(url=url, headers=header)
                    except Exception:
                        time.sleep(2)
                        ourrequest = requests.get(url=url, headers=header)

                    if (ourrequest.status_code == 200):
                        soup = bs.BeautifulSoup(ourrequest.content, "lxml")
                        for div in soup.find_all(html_list[i], id=class1[i]):
                            str = div.text

                            str = str.replace("\n", "")
                            str = str.replace("\t", "")
                            par = str.split(".")
                            for line in par:
                                str1 = "great months"
                                str2 = "best season"
                                str3 = "best time"
                                str4 = "best months"
                                str5 = "ideal time"
                                str6 = "most favourable time"
                                if line.lower().find(str1) != -1 or line.lower().find(str2) != -1 or line.lower().find(
                            str3) != -1 or line.lower().find(str4) != -1 or line.lower().find(
                        str5) != -1 or line.lower().find(str6) != -1:

                                    line = line.split()
                                    count = 0
                                    for word in line:
                                        try:
                                            if word in months and line[count + 2] in months:
                                                data[state][place][website[i]] = line[count] + " to " + line[count + 2]
                                                print("ok")
                                                break
                                        except Exception:
                                            continue
                                        count += 1
                    ourrequest.close()
                except Exception:
                    continue
        print(data[state])
    with open("tourism_data_3.json", "w") as outfile:
        json.dump(data, outfile)
'''
fp=open("tourism_data_3.json","r")
data=json.load(fp)
print(data)
'''

website = [ "holidify"]
host = [ "www.holidify.com"]
url_list1 = ["https://www.holidify.com/places/"]
url_list2 = [ "/weather.html","/best-time-to-visit", "/best-time-to-visit.html", "/best-time-to-visit.html", "/best-time-to-visit.html",
             "-best-time-to-visit.aspx"]
html_list = [ "div","div", "p", "div", "div", "td"]
class1 = ["intl-weather-desc","my-wrap p25-0 fs13 content lh25 fl conDiv", "infotxt", "col-md-12 col-xs-12 middleSection",
          "bestTimeInfoLft", "middleTopPanel"]

'''
website = [ "journeymart"]
host = ["journeymart.com"]
url_list1 = [ "http://journeymart.com/de/india/karnataka/"]
url_list2 = [ "-best-time-to-visit.aspx"]
html_list = ["td"]
class1 = ["middleTopPanel"]
'''
for i in range(len(website)):
    # if i==2 or i==3:
    #  time.sleep(5)

    print("")
    print(website[i])
    print("")

    header["Host"] = host[i]
    for state in data.keys():
        for place in data[state].keys():
        # if i == 2 :
        #   time.sleep(3)
            if len(place.split())>1:
                u = place.replace(" ", "-")
                u = u.lower()
                print(place)
                if(website[i]=="journeymart"):
                    s=state.replace(" ","-")
                    s=s.lower()
                    url="http://journeymart.com/de/india/"+s+"/"+u + url_list2[i]
                    print(url)
                else:
                    url = url_list1[i] + u + url_list2[i]

                try:
                    try:
                        ourrequest = requests.get(url=url, headers=header)

                    except Exception:
                        time.sleep(2)
                        ourrequest = requests.get(url=url, headers=header)
                    if (ourrequest.status_code == 200):
                        soup = bs.BeautifulSoup(ourrequest.content, "lxml")
                        for div in soup.find_all(html_list[i], class_=class1[i]):
                            str = div.text

                            str = str.replace("\n", "")
                            str = str.replace("\t", "")
                            par = str.split(".")
                            for line in par:
                                str1 = "great months"
                                str2 = "best season"
                                str3 = "best time"
                                str4 = "best months"
                                str5 = "ideal time"
                                str6 = "most favourable time"
                                if line.lower().find(str1) != -1 or line.lower().find(str2) != -1 or line.lower().find(
                            str3) != -1 or line.lower().find(str4) != -1 or line.lower().find(
                        str5) != -1 or line.lower().find(str6) != -1:

                                    line = line.split()
                                    count = 0
                                    for word in line:
                                        try:
                                            if word in months and line[count + 2] in months:
                                                data[state][place][website[i]] = line[count] + " to " + line[count + 2]
                                                break
                                        except Exception:
                                            continue
                                        count += 1
                    ourrequest.close()
                except Exception:
                    continue
        print(data[state])
    with open("tourism_data_3.json", "w") as outfile:
        json.dump(data, outfile)

with open("tourism_data_3.json", "w") as outfile:
    json.dump(data, outfile)
print("finish")
# file_data.write(str(data))


'''
print('ourrequest["data"]["parent"]["notes"]["Best Season"]')
data[place]["district"] = ourrequest["data"]["parent"]["notes"]["District"]
print(ourrequest["data"]["parent"]["notes"]["District"])
'''