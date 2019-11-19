from xlutils.copy import copy
import xlrd

file1 = "test/files/环境清单及各渠道负责人.xlsx"
save_file = "test/files/save_file.xlsx"

rb = xlrd.open_workbook(file1,formatting_info=True)
wb = copy(rb)
ws = wb.get_sheet(1)
for rx in range(ws.nrows):
  print(ws.row(rx))

ws.write(1,1,"changed")
wb.save(save_file)







