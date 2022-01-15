from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Anshir\Desktop\\Final Year Project\\favicon.ico",
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
updates = soup.title.get_text().split(' ')   
message = f"In India Total Cases are: {updates[2]} and Total Deaths are: {updates[5]}"
notifyMe("Covid-19 update is here... INDIA",message)
        #time.sleep(86400)