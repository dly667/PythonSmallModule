import win32com.client

book = win32com.client.Dispatch('Excel.Application').Workbooks.Open(r'D:\01.xls')
sht = book.Worksheets('Sheet1')
sht.Rows(17).Delete()
sht.SaveAs(r'D:\999.xls')


