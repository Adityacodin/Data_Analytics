from bs4 import BeautifulSoup
import requests

def convert(duration_string):
    ls = duration_string.split(' ')
    num = int(ls[0])*60 + int(ls[2])
    return num


imdb_link = input("IMDB_link: ")
headers = {"User-Agent": "Mozilla/5.0"}
html_text = requests.get(imdb_link,headers = headers).text
soup = BeautifulSoup(html_text,'html.parser')

# LANGUAGE
parent = soup.find("li", {"data-testid":"title-details-languages"})
lang = parent.find("a",{"class":"ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"})
language = lang.text
print(language)

# # YEAR
parent = soup.find("li", {"data-testid":"title-details-releasedate"})
release_date = parent.find("a", {"class" : "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"})
year = release_date.text.split(" ")[2]

# # COUNTRY
parent = soup.find("li",{"data-testid":"title-details-origin"})
origin = parent.find("a",{"class" : "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"})
country = origin.text

# # DURATION
parent = soup.find("li",{"data-testid":"title-techspec_runtime"})
duration_in_words= parent.find("div", {"class" : "ipc-metadata-list-item__content-container"})
duration = convert(duration_in_words.text)
print(duration)

# COLOR
parent = soup.find("li",{"data-testid":"title-techspec_color"})
color = parent.find("div",{"class" : "ipc-metadata-list-item__content-container"}).text
print(color)

# ASPECT RATIO
parent = soup.find("li",{"data-testid":"title-techspec_aspectratio"})
aspect_ratio = parent.find("span",{"class" : "ipc-metadata-list-item__list-content-item"}).text
print(aspect_ratio[:4])

# GROSS AND BUDGET
bf_obj = soup.find_all("div", class_ = "sc-f65f65be-0 dQVJPm")
spans = bf_obj[-3].find_all("span",class_= "ipc-metadata-list-item__list-content-item")
gross = spans[0].text 
budget = spans[1].text
print(gross,budget)

# # ACTORS AND DIRECTORS
ul = soup.find("div", class_= "sc-70a366cc-2 bscNnP")
li = ul.find_all('a',class_ = "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")
director = li[0].string
actor1 = li[-1].string if li[-1].string else "Na"
actor2 = li[-2].string if li[-2].string else "Na" 
actor3 = li[-3].string if li[-3].string else "Na"     
print(director,actor1,actor2,actor3)
