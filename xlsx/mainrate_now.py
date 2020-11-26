import twder
import xlsxwriter
def get_information():
    i = 0
    workbook = xlsxwriter.Workbook('19rate1.xls')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 1, "幣別")
    worksheet.write(0, 2, "現金1")
    worksheet.write(0, 3, "現金2")
    for value in twder.currencies():
        worksheet.write(i+1, 0, i)
        worksheet.write(i+1, 1, value)
        worksheet.write(i+1, 2, twder.past_day(value)[len(twder.past_day(value)-1)][3])
        worksheet.write(i+1, 3, twder.past_day(value)[len(twder.past_day(value)-1)][4])
        i+=1
        print("writting %s successfully"%value)
        print("-------------------------------")
    workbook.close()

if __name__ == "__main__":
    get_information()