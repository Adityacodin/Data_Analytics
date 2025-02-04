import requests
from bs4 import BeautifulSoup

def write_director_name(director_name):
    for record in director_name:
        print(record['title'],record['director'])

def get_director_name(mov):
    dir_name = []
    for movie in mov:
        movie_title = movie+" (film)"
        wiki_url = f"https://en.wikipedia.org/wiki/{movie_title.replace(' ', '_')}"
        
        headers = {"User-Agent" : "Mozilla/5.0"}
        response = requests.get(wiki_url,headers = headers)
        sp = BeautifulSoup(response.text,"html.parser")

        infobox = sp.find("table",class_ = "infobox")

        if infobox:
            for row in infobox.find_all("tr"):
                header = row.find("th")
                data = row.find("td")

                if header and data:
                    key = header.text.strip()
                    value = data.text.strip()
                    if key == "Directed By":
                        dir_name.append({"title":movie ,"director":value})
                        print(key,value)
        else:
            dir_name.append({"title":movie ,"director":""})
    return dir_name



def main():
    with open("na_director.txt" ,"r" , encoding  = "ANSI",newline = '')  as file:
        movie = [line.strip() for line in file]
    director_name = get_director_name(movie)
    write_director_name(director_name)


if __name__ == "__main__":
    main()