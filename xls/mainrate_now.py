import twder
from xlwt import Workbook
def get_information():
    i = 0
    wb = Workbook()
    worksheet = wb.add_sheet("Sheet1")
    worksheet.write(0, 1, "幣別")
    worksheet.write(0, 2, "現金1")
    worksheet.write(0, 3, "現金2")
    for value in twder.currencies():
        worksheet.write(i+1, 0, i)
        worksheet.write(i+1, 1, value)
        worksheet.write(i+1, 2, twder.now(value)[3])
        worksheet.write(i+1, 3, twder.now(value)[4])
        i+=1
        print("writting %s successfully"%value)
        print("-------------------------------")
    wb.save("19rate1.py")

if if __name__ == "__main__":
    get_information()