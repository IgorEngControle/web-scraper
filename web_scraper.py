import requests
from bs4 import BeautifulSoup
import pandas as pd


#extract information of climate of tag day extract from seven_days
def get_information_tag(day):
    # print(tonight.prettify())
    period = day.find(class_="period-name").get_text()
    short_desc = day.find(class_="short-desc").get_text()
    temp = day.find(class_="temp").get_text()
    elem_list = []

    print(period)
    elem_list.append(period)
    print(short_desc)
    elem_list.append(short_desc)
    print(temp)
    elem_list.append(temp)

    img = day.find('img')
    desc = img['title']
    print(desc)
    elem_list.append(desc)

    return elem_list

#did the request GET from page
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XFB3ZnUrLCK')

#tranform in Beatifulsoup object
soup = BeautifulSoup(page.content, 'html.parser')

#colect the part of html with such 'id'
seven_day = soup.find(id="seven-day-forecast")

#select the class of this id
forecast_items = seven_day.find_all(class_="tombstone-container")

# tonight = forecast_items[0]

forecast_list = []
for day in forecast_items:
    forecast_list.append(get_information_tag(day))

df_to_save = pd.DataFrame(forecast_list, columns=['day','short_desc','temp','desc'])

df_to_save.to_csv('example', sep=",")

# Remover links inferiores

# friend_name_list = soup.find(class_='BodyText')
# artist_name_list_items = firne.find_all('a')
#
# for artist_name in artist_name_list_items:
#     print(artist_name.prettify())