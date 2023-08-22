import pandas as pd
from datetime import datetime 
import requests
from bs4 import BeautifulSoup as BS
from requests import session
s = session()

s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/116.0'
url = "https://weather.com/en-IN/weather/today"

requests = s.get(url)

soup = BS(requests.text,'html.parser')

today = datetime.now()
date = today.strftime('%d %b %Y')

place =  soup.find('h2','Card--cardHeading--2H1-_').text.replace("Today's Forecast for ","")
currrentTemp = soup.find('span','TodayDetailsCard--feelsLikeTempValue--2icPt').text + str('C')
tempRange = soup.find('div','WeatherDetailsListItem--wxData--kK35q').text
humidity = soup.find('span',attrs={'data-testid':'PercentageValue'}).text
wind = soup.find('span','Wind--windWrapper--3Ly7c undefined').text.replace("Wind Direction","").strip().replace('\xa0','')
weather = soup.find('div','CurrentConditions--phraseValue--mZC_p').text


d = {
    "PLACE" : place, 
    "DATE" : date, 
    "TEMPERATURE" : tempRange, 
    "HUMIDITY": humidity, 
    "WIND" : wind, 
    "WEATHER": weather
}

l = list()
l.append(d)

df = pd.DataFrame(l)
df.to_csv(f"{date} weather report.csv",index=False)
