import csv
import random

headers = ["header1", "header2", "header3", "header4", "header5", "header6", "header7", "header8", "header9",
           "header10", "header11"]

data = ["Adam", "Bob", "Claire", "Danny", "Emily", "Frank", "George", "Harry", "Ian", "Jack", "Kathrin"]

final_data = [data] * 100000
final_data[0] = headers


def create_csv_data():
    with open("sample.csv", "w") as csvFile:
        writer = csv.writer(csvFile)
        for r in final_data:
            writer.writerow(r)
            random.shuffle(r)


if __name__ == "__main__":
    create_csv_data()

