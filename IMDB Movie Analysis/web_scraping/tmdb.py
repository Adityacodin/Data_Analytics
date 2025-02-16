# # 485feaaeabf90be20853ae50365d5670
import requests
import csv

inpt = []
output = []
with open("na_records.csv","r" , encoding="ANSI", newline = "") as r_file:
    reader = csv.DictReader(r_file)
    for row in reader:
        inpt.append(row["movie_title"])


start = -100
end = 0
index = 0
for i in range(12):
    start += 100
    end += 100
    print(f"Round {i} : start = {start},end = {end}" )
    output = []
    for movie in inpt[1200:1288]:
        print(f"Record No.:{index}")
        API_KEY = "485feaaeabf90be20853ae50365d5670"
        MOVIE_NAME = movie.strip()

        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={MOVIE_NAME}"
        search_response = requests.get(search_url).json()

        if "results" in search_response and search_response["results"]:
            movie_id = search_response["results"][0]["id"]
        else:
            print(f"Error: No results found for {MOVIE_NAME}")
            continue

        details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        details_response = requests.get(details_url).json()
        budget = details_response.get("budget", "N/A")
        revenue = details_response.get("revenue", "N/A")
        language = details_response.get("original_language", "N/A")
        country = details_response.get("origin_country","N/A")[0] if details_response.get("origin_country","N/A") != "N/A" else "N/A"
        release_date = details_response.get("release_date","N/A")
        runtime = details_response.get("runtime","N/A")
        year = release_date[:4] if release_date != "N/A" else release_date


        credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}"
        credits_response = requests.get(credits_url).json()
        director = "N/A"
        for crew_member in credits_response.get("crew", []):
            if crew_member["job"] == "Director":
                director = crew_member["name"]
                break

        actors = [actor["name"] for actor in credits_response.get("cast", [])[:3]]
        

        output.append({"title":MOVIE_NAME,"director":director,"budget":budget,"gross":revenue,"language":language,"country":country,"year":year,"runtime":runtime,"actors":str(', '.join(actors))})
        index+=1

    try:
        with open("scraped_records"+str(12)+".csv","w",encoding = "ANSI",newline = "") as w_file:
            writer = csv.DictWriter(w_file,fieldnames = ["title","director","budget","gross","language","country","year","runtime","actors"])
            writer.writeheader()
            for record in output:
                writer.writerow(record)
    except:
        print(f"Error Occured, Movie:{MOVIE_NAME}")
    exit()
        

# print(f"Title: {MOVIE_NAME}")
# print(f"Director: {director}")
# print(f"Budget: ${budget:,}")
# print(f"Gross Revenue: ${revenue:,}")
# print(f"Language: {language}")
# print(f"Country: {country}")
# print(f"Year: {year}")
# print(f"Runtime: {runtime}")
# print(f"Actors: {', '.join(actors)}")
