import requests
from bs4 import BeautifulSoup


#print name of profile
def print_name (soup):
    fb_profile_cover = soup.find(id="fbProfileCover")

    profile_name = fb_profile_cover.text

    print(profile_name)

page = requests.get('https://www.facebook.com/100004677967857')

#tranform in Beatifulsoup object
soup = BeautifulSoup(page.content, 'html.parser')

print_name(soup)


print(soup.prettify())




#colect the part of html with such 'id'
