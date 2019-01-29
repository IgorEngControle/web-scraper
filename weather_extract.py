import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_information(row_weather):
    #day

    weather_day_list = []

    day = row_weather.find(class_ = 'day-detail clearfix').get_text()
    weather_day_list.append(day)
    description = row_weather.find(class_ = 'description').get_text()
    weather_day_list.append(description)
    temp = row_weather.find(class_ = "temp").get_text()
    weather_day_list.append(temp)
    precip = row_weather.find(class_ = "precip").get_text()
    weather_day_list.append(precip)
    wind = row_weather.find(class_ = "wind").get_text()
    weather_day_list.append(wind)
    humidity = row_weather.find(class_ = "humidity").get_text()
    weather_day_list.append(humidity)

    return weather_day_list



page = requests.get('https://weather.com/pt-BR/clima/10dias/l/BRXX4353:1:BR')

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(id= 'twc-scrollabe')


weather_table = table.find(class_ = 'twc-table')

row_weather = weather_table.find('tr',class_ = "clickable closed")


forecast_list = []


while (row_weather != None):
    forecast_list.append(get_information(row_weather))
    row_weather = row_weather.next_sibling

df_to_save = pd.DataFrame(forecast_list, columns=['day','description','temp','precip','wind','humidity'])
df_to_save.to_csv('weather_claudio.csv', sep=",")
