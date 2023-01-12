import csv
import pandas as pd
import twder

def get_information():
    df = pd.read_json('https://www.bankchb.com/frontend/jsp/getG0100_query.jsp?v=1611916729375')
    with open("19rate1.csv", "w", encoding='UTF8', newline='') as csvfile:
        i = 0
        writer = csv.writer(csvfile)
        for data in df["datas"]:
            value = data["curname"].split('(', 1)[1].split(')', 1)[0]
            writer.writerow([i, 
            value, 
            data["buy"], 
            data["sell"]])
            i+=1
            print("writting %s successfully"%value)
            print("-------------------------------")
    create_txtinfor()

def create_txtinfor():
    with open('mainrate.txt', "w",  encoding='UTF8', newline='') as file:
        file.write("mainrate getdata successfully")

if __name__ == "__main__":
    get_information()