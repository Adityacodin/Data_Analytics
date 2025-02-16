import csv

def mark_na(row,headers = ["color","director_name","num_critic_for_reviews","duration","director_facebook_likes","actor_3_facebook_likes","actor_2_name","actor_1_facebook_likes","gross","genres","actor_1_name","movie_title","num_voted_users","cast_total_facebook_likes","actor_3_name","facenumber_in_poster","plot_keywords","movie_imdb_link","num_user_for_reviews","language","country","content_rating","budget","title_year","actor_2_facebook_likes","imdb_score","aspect_ratio","movie_facebook_likes"]):
    for header in headers:
        if row[header] == "":
            row[header] = "N/A"

scraped = []
with open("final.csv","r",encoding = "ANSI", newline = '') as r_file:
    reader = csv.DictReader(r_file)
    for row in reader:
        scraped.append(row)
    
na = []
with open("na_records.csv","r", encoding = "ANSI",newline = '') as r_file:
    reader = csv.DictReader(r_file)
    for row in reader:
        na.append(row)

na_index = 0
sc_index = 0
output = []
while True:
    if na_index == len(na) or sc_index == len(scraped):
        break
    if na[na_index]["movie_title"].strip() == scraped[sc_index]["title"].strip():
        na[na_index]["director_name"] = scraped[sc_index]['director']
        na[na_index]["budget"] = scraped[sc_index]['budget']
        na[na_index]["gross"] = scraped[sc_index]['gross']
        na[na_index]["budget"] = scraped[sc_index]['budget']
        na[na_index]["language"] = scraped[sc_index]['language']
        na[na_index]["country"] = scraped[sc_index]['country']
        na[na_index]["title_year"] = scraped[sc_index]['year']
        na[na_index]["duration"] = scraped[sc_index]['runtime']
        mark_na(na[na_index])
        print(f'Corrected {scraped[sc_index]["title"].strip()}')
        output.append(na[na_index])
        na_index += 1
        sc_index += 1
    else:
        na_index+=1
        print(f'Skipped {na[na_index]["movie_title"].strip()}')

with open("final_scraped.csv","w",encoding = "ANSI",newline = "")  as w_file:
    print(f"Writing {len(output)} records in the file")
    writer = csv.DictWriter(w_file, fieldnames = ["color","director_name","num_critic_for_reviews","duration","director_facebook_likes","actor_3_facebook_likes","actor_2_name","actor_1_facebook_likes","gross","genres","actor_1_name","movie_title","num_voted_users","cast_total_facebook_likes","actor_3_name","facenumber_in_poster","plot_keywords","movie_imdb_link","num_user_for_reviews","language","country","content_rating","budget","title_year","actor_2_facebook_likes","imdb_score","aspect_ratio","movie_facebook_likes"])
    writer.writeheader()
    for record in output:
        writer.writerow(record)




    