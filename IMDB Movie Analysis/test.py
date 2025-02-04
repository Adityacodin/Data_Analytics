# from imdb import IMDb
# from word2number import w2n

# ia = IMDb()
# movie = ia.search_movie('Should\'ve Been Romeo')[0]  # Search for movie
# ia.update(movie)  # Fetch full details

# print(f"Title: {movie['title']}")
# print(f"Year: {movie['year']}")
# print(f"Director: {movie['director'][0]}")
# print(f"Genres: {', '.join(movie['genres'])}")
# print(f"IMDb Rating: {movie.get('rating')}")
# print(f"Runtime: {movie.get('runtimes')[0]} min")
# print(f"Plot: {movie.get('plot outline')}")

# print('camela\'s')

# ia = IMDb()
# ip = ['Hannibal']
# op = []
# for mv in ip:
#     mov = ia.search_movie(mv)[0]
#     ia.update(mov)
#     print(f"Title: {mov['title']}")
#     print(f"Director: {mov['year']}")


import requests
from bs4 import BeautifulSoup

# Movie Wikipedia URL (change movie title as needed)
with open("na_director.txt" ,"r" , encoding  = "ANSI",newline = '')  as file:
    mov = [line.strip() for line in file]

for movie in mov:
    movie_title = movie+" (film)"
    wiki_url = f"https://en.wikipedia.org/wiki/{movie_title.replace(' ', '_')}"

    # Fetch page content
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(wiki_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract Infobox (structured movie details)
    infobox = soup.find("table", class_="infobox")

    # Extract rows from the infobox
    if infobox:
        for row in infobox.find_all("tr"):
            header = row.find("th")
            data = row.find("td")

            if header and data:
                key = header.text.strip()
                value = data.text.strip()
                if(key == "Directed by"):
                    print(f"{key}: {value}")
    else:
        print("No infobox found!")

