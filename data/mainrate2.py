import csv
import pandas as pd
import datetime

def getCurrJson():
    df = pd.read_json('https://portal.sw.nat.gov.tw/APGQ/GC331!downLoad?formBean.downLoadFile=CURRENT_JSON')
    sDate = str(df.iloc[0,0])
    eDate = str(df.iloc[0,1])
    with open("19rate2.csv", "w", encoding='UTF8', newline='') as csvfile:
        i = 0
        writer = csv.writer(csvfile)
        for rowIdx in df.index:
            dic = df.iloc[rowIdx, 2]
            writer.writerow([i, 
                    dic['code'], 
                    dic['buyValue'], 
                    dic['sellValue'],
                    sDate,
                    eDate])
            i+=1
            print("writting %s successfully"%dic['code'])
            print("-------------------------------")
    create_txtinfor()

def create_txtinfor():
    with open('mainrate2.txt', "w",  encoding='UTF8', newline='') as file:
        file.write("mainrate2 getdata successfully")

if __name__ == '__main__':
    getCurrJson()