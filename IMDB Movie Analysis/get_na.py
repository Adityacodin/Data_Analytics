import csv

def na_retrieve(file_name,output_file_name,header_name):
    output_list = []
    with open(file_name, "r", newline="",encoding = "ANSI") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row[header_name].strip() == "":
                output_list.append(row["movie_title"].strip())
    print(output_list)
    with open(output_file_name,"w",encoding = "ANSI") as w_file:
        for record in output_list:
            w_file.write(record+"\n")

def main():
    file_name = input("File name: ").strip()
    op_file_name = input("Output file name: ").strip()
    header_name = input("Header name: ").strip()
    na_retrieve(file_name,op_file_name,header_name)
        

if __name__ == "__main__":
    main()