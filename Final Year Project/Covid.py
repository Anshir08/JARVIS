from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "D://Users//Anshir//Desktop//Some Folder//Final Year Project//favicon.ico",
        
        timeout = 30
    )

def getData(url):
    return requests.get(url).text

# while True:
myHtmlData = getData("https://www.worldometers.info/coronavirus/country/india/")
soup = BeautifulSoup(myHtmlData, 'html.parser')
#print(soup.prettify())
# for t in soup.find_all('table'):
#     print(t.get_text())
# updates = soup.title.get_text().split(' ') 
updates = soup.find_all("div", class_="maincounter-number")
cases = updates[0].text
deaths = updates[1].text
recovered = updates[2].text
print(recovered)
message = f"Globally Total Cases are: {cases}, Total Deaths are: {deaths} and Total recovered are: {recovered} "
notifyMe("Covid-19 update is here... INDIA",message)
        #time.sleep(86400)