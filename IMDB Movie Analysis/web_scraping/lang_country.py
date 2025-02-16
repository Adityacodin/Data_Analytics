import csv

inpt = []
with open("final_scraped.csv","r", encoding = "ANSI", newline  ="") as r_file:
    reader = csv.DictReader(r_file)
    for row in reader:
        inpt.append(row)
    
country_codes = {
    "AU": "Australia",
    "US":"USA",
    "JP":"Japanese",
    "GB":"UK",
    "FR":"France",
    "MX":"Mexico",
    "PE": "Peru",
    "DE": "Germany",
    "KR": "South Korea",
    "CA": "Canada",
    "IN": "India",
    "CN": "China",
    "RU": "Russia",
    "BE": "Belgium",
    "TH": "Thailand",
    "ES": "Spain",
    "SU": "Soviet Union",  # Former country
    "IT": "Italy",
    "IE": "Ireland",
    "SE": "Sweden",
    "NL": "Netherlands",
    "BR": "Brazil",
    "DK": "Denmark",
    "EG": "Egypt",
    "BT": "Bhutan",
    "SD": "Sudan",
    "PH": "Philippines",
    "NZ": "New Zealand",
    "KG": "Kyrgyzstan",
    "ZA": "South Africa",
    "IL": "Israel",
    "UR": "Pakistan",  # Not a valid modern country code
    "AR": "Argentina"
}

language_codes = {
    "en": "English",
    "ja": "Japanese",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "te": "Telugu",
    "zh": "Mandarin",
    "cn": "Mandarin",
    "ru": "Russian",
    "th": "Thai",
    "ta": "Tamil",
    "ko": "Korean",
    "hi": "Hindi",
    "ca": "Catalan",
    "it": "Italian",
    "sv": "Swedish",
    "da": "Danish",
    "ar": "Arabic",
    "dz": "Dzongkha",
    "ky": "Kyrgyz",
    "he": "Hebrew",
    "ur": "Urdu",
    "fa": "Farsi",
    "pt": "Portuguese"
}
for record in inpt:
    record["language"] = language_codes[record["language"]]
    record["country"] = country_codes[record["country"]]

with open("final.csv" , "w" ,encoding= "ANSI", newline = "") as w_file:
    writer = csv.DictWriter(w_file,fieldnames=["color","director_name","num_critic_for_reviews","duration","director_facebook_likes","actor_3_facebook_likes","actor_2_name","actor_1_facebook_likes","gross","genres","actor_1_name","movie_title","num_voted_users","cast_total_facebook_likes","actor_3_name","facenumber_in_poster","plot_keywords","movie_imdb_link","num_user_for_reviews","language","country","content_rating","budget","title_year","actor_2_facebook_likes","imdb_score","aspect_ratio","movie_facebook_likes"])
    writer.writeheader()
    for record in inpt:
        writer.writerow(record)