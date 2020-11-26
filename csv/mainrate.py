import csv
import twder
def get_information():
     with open("19rate.csv", newline='') as csvfile:
        i = 0
        writer = csv.writer(csvfile)
        for value in twder.currencies():
            writer.writerow([i, value, twder.past_day(value)[len(twder.past_day(value)-1)][1], twder.past_day(value)[len(twder.past_day(value)-1)][2]])
            i+=1
            print("writting %s successfully"%value)
            print("-------------------------------")

if __name__ == "__main__":
    get_information()