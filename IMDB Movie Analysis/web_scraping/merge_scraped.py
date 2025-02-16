import csv

def main():
    records = []
    for i in range(0,13):
        with open("scraped_records"+str(i)+".csv", "r", encoding = "ANSI", newline = "") as r_file:
            reader  = csv.DictReader(r_file)
            for row in reader:
                records.append(row)
    print(f"Total records: {len(records)}")

    with open("final.csv","w", encoding= "ANSI",newline="") as w_file:
        writer = csv.DictWriter(w_file, fieldnames = ["title","director","budget","gross","language","country","year","runtime","actors"])
        writer.writeheader()
        for record in records:
            writer.writerow(record)
    

if __name__ == "__main__":
    main()