# import requests
# from bs4 import BeautifulSoup
import csv

# def get_imdb_details(url):
#     headers = {"User-Agent": "Mozilla/5.0"}
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, "html.parser")

#     # Extract Title
#     title = soup.find("h1").text.strip() if soup.find("h1") else "N/A"

#     # Extract IMDb director
#     director = soup.find("a", {"class":"ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"}).text if soup.find("a", {"class":"ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"}) else "N/A"

#     rating = soup.find("a", {"class":"pc-link.ipc-link--baseAlt ipc-link--inherit-color"}).text if soup.find("a", {"class":"pc-link ipc-link--baseAlt ipc-link--inherit-color"}) else "N/A"

#     # Extract Genre(s)
#     genres = [g.text for g in soup.find_all("span", class_="ipc-chip__text")]

#     return {"Title": title, "director": director, "rating":rating, "Genres": genres}

# # Example usage
# imdb_url = "http://www.imdb.com/title/tt0499549/?ref_=fn_tt_tt_1"  # Example: The Shawshank Redemption
# print(get_imdb_details(imdb_url))

with open("na_records.csv","r" , encoding="ANSI", newline = "") as r_file:
    reader = csv.DictReader(r_file)
    for row in reader:
        print(row["movie_title"].strip())