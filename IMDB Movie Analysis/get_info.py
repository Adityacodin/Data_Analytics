from imdb import IMDb
import csv

def get_info(f_name):
    ls= []
    with open(f_name , "r", encoding = "ANSI", newline="") as file:
        for line in file:
            ls.append(line.strip())
    return ls

# Should've Been Romeo
# Miami Vice

def main():
    file_name = input("file name: ")
    ip = get_info(file_name)
    try: 
        ia = IMDb()
        op = []
        for mv in ip:
            mov = ia.search_movie(mv)[0]
            ia.update(mov)
            if 'year' in mov.keys():
                op.append({'title':str(mov.get("title")), 'year':mov["year"]})
                print(str(mov.get("title")),mov['year'])
            else:
                op.append({'title':str(mov.get("title")), 'year':''})
                print(str(mov.get("title")))
    except:
        print("error")
        with open("year.csv", "w", encoding="ANSI",newline = '') as w_file:
            fieldnames = ['title','year']
            writer = csv.DictWriter(w_file,fieldnames=fieldnames)
            writer.writeheader()
            for year in op:
                writer.writerow(year) 
    else:
        with open("year.csv", "w", encoding="ANSI",newline = '') as w_file:
            fieldnames = ['title','year']
            writer = csv.DictWriter(w_file,fieldnames=fieldnames)
            writer.writeheader()
            for year in op:
                writer.writerow(year)

if __name__ == "__main__":
    main()