import csv
headers = ["color","director_name","num_critic_for_reviews","duration","director_facebook_likes","actor_3_facebook_likes","actor_2_name","actor_1_facebook_likes","gross","genres","actor_1_name","movie_title","num_voted_users","cast_total_facebook_likes","actor_3_name","facenumber_in_poster","plot_keywords","movie_imdb_link","num_user_for_reviews","language","country","content_rating","budget","title_year","actor_2_facebook_likes","imdb_score","aspect_ratio","movie_facebook_likes"]

with open("imdb_ex.csv" , "r", encoding = "ANSI") as r_file:
    reader = csv.DictReader(r_file)
    output = []
    for row in reader:
        for header in headers:
            if row[header] == "":
                output.append(row)
                break
    print(f"{len(output)} empty records found")

with open("na_records.csv", "w", encoding="ANSI",newline = "") as w_file:
    writer = csv.DictWriter(w_file, fieldnames = headers)
    writer.writeheader()
    for record in output:
        writer.writerow(record)