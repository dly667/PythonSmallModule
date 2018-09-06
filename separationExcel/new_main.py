import xlrd
import  time
import xlwt
from xlutils.filter import process, XLRDReader, XLWTWriter
import win32com.client
class Transform(object):
    def __init__(self):
        self.row_col_dict = dict()
        pass
    def read(self):
        workbook = xlrd.open_workbook(u'数据格式表.xlsx',on_demand=True)
        sheet_names = workbook.sheet_names()

        self.temp_book = list()
        for sheet_name in sheet_names:
            sheet2 = workbook.sheet_by_name(sheet_name)

            print(sheet_name)
            # 获取总行数
            nrows = sheet2.nrows
            # 获取销售列的数据
            if sheet_name == "交易月综合表":
                cols = sheet2.col_values(12)
                self.saleNameList = list(set(cols))
                self.saleNameList.remove("所属销售")
                self.saleNameList.remove("")

            temp_sheet = list()
            for row_num in range(2,nrows-1):
                rows = sheet2.row_values(row_num)  # 获取第四行内容
                temp_sheet.append(rows)
            # cols = sheet2.col_values(1)  # 获取第二列内容
            self.temp_book.append({"sheet_name":sheet_name,
                                   "second_line":sheet2.row_values(1),
                                   "last_line": sheet2.row_values(nrows-1),
                                   "data":temp_sheet})


    def deal_with(self):


        pass

    def comprehensive_table(self):
        new_file = dict()
        for saleName in self.saleNameList:
            pass
    def detail_table(self):
        pass
    # 取出销售名为XXX的所有数据
    def getBookBySaleName(self,saleName):
        new_book = list()
        self.row_col_dict[saleName] = {}
        for sheet in self.temp_book:
            self.row_col_dict[saleName][sheet["sheet_name"]] = []
            if sheet["sheet_name"] == "交易月综合表":
                new_data = list()
                for index,row in enumerate( sheet["data"]):
                    if row[12] == saleName:
                        new_data.append(row)

                    else:
                        # 获得不符合此销售名字的行列号
                        self.row_col_dict[saleName][sheet["sheet_name"]].append(index + 3)
                new_book.append(
                    {'sheet_name': sheet["sheet_name"], 'second_line': sheet["second_line"], "data": new_data})
                #break
            else:
                new_data = list()

                for index,row in enumerate( sheet["data"]):
                    if row[13] == saleName:
                        new_data.append(row)

                    #获得不符合此销售名字的行列号
                    else:
                        self.row_col_dict[saleName][sheet["sheet_name"]].append(index+3)

                new_book.append(
                    {'sheet_name': sheet["sheet_name"], 'second_line': sheet["second_line"], "data": new_data})
        return new_book
    def deleteRow(self,sn):
        data = self.row_col_dict
        print(data,11)
        book = win32com.client.Dispatch('Excel.Application').Workbooks.Open(r'G:\python\PythonSmallModule\separationExcel\31.xlsx')
        sht = book.Worksheets("Sheet1")

        for i in range(1,2):
            # a = sht.Range(sht.Cells(1,1),sht.Cells(24,1))
            sht.Range(sht.Cells(1, 1), sht.Cells(28,2)).Delete()
        book.SaveAs(r'G:\python\PythonSmallModule\separationExcel\{}.xlsx'.format(321))
        print(sht.Rows(1))
        # for k,v in data[sn].items():
        #
        #     sht = book.Worksheets("08.28")
        #     print(sht.Rows(10))
        #     for i in v:
        #         #删除单行数据
        #         # print("Rows",sht.Rows(i))
        #         # time.sleep(0.1)
        #         sht.Rows(i).Delete()

        # book.SaveAs(r'G:\python\PythonSmallModule\separationExcel\{}.xlsx'.format(sn))

    def main(self):
        self.read()
        # print(self.saleNameList)
        for sn in self.saleNameList:
            self.getBookBySaleName(sn)
            self.deleteRow(sn)
            break
        # print(self.row_col_dict)
        # self.deal_with()

if __name__ == '__main__':
    Transform().main()