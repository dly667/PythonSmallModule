import xlrd
import xlwt
from xlutils.filter import process, XLRDReader, XLWTWriter

class Transform(object):
    def __init__(self):
        pass
    def read(self):
        workbook = xlrd.open_workbook(u'数据格式表.xlsx', formatting_info=True, on_demand=True)
        sheet_names = workbook.sheet_names()
        self.rd = workbook
        self.temp_book = list()
        for sheet_name in sheet_names:
            sheet2 = workbook.sheet_by_name(sheet_name)
            self.rds = sheet2
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

        print(self.temp_book)
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

        for sheet in self.temp_book:
            print("sheet:",sheet)
            if sheet["sheet_name"] == "交易月综合表":
                new_data = list()
                for row in sheet["data"]:
                    if row[12] == saleName:
                        new_data.append(row)

                new_book.append(
                    {'sheet_name': sheet["sheet_name"], 'second_line': sheet["second_line"], "data": new_data})
                #break
            else:
                new_data = list()
                for row in sheet["data"]:
                    if row[13] == saleName:
                        new_data.append(row)

                new_book.append(
                    {'sheet_name': sheet["sheet_name"], 'second_line': sheet["second_line"], "data": new_data})
        return new_book
    def myWrite(self,book,book_name):
        # 设置样式
        # style = xlwt.XFStyle()
        # font = xlwt.Font()
        # font.name = 'SimSun'  # 指定“宋体”
        # style.font = font

        # 1.表头样式
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = '宋体'  # 指定“宋体”
        font.bold = True
        font.height = 0x00DC
        style.font = font
        al = xlwt.Alignment()
        al.horz = 0x02  # 设置水平居中
        al.vert = 0x01  # 设置垂直居中
        style.alignment = al

        # 2.数据样式
        style2 = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = '宋体'  # 指定“宋体”

        font.height = 0x00DC
        style2.font = font
        al = xlwt.Alignment()
        al.horz = 0x02  # 设置水平居中
        al.vert = 0x01  # 设置垂直居中
        style2.alignment = al

        s = self.copy2(self.rd)
        styles = s[self.rds.cell_xf_index(2, 2)]

        # rb.release_resources()  # 关闭模板文件

        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding='utf-8')
        for sheet2 in book:
            # 创建一个worksheet
            worksheet = workbook.add_sheet(sheet2["sheet_name"],cell_overwrite_ok=True)

            # 写入excel
            # 参数对应 行, 列, 值
            for index,item in enumerate(sheet2["second_line"]):
                # 设置列宽
                worksheet.col(index).width = 4333
                # print(index,item)
                worksheet.write(1, index, item,style)

            for row_num,row in enumerate(sheet2["data"]):


                for col_num,col in enumerate(row):
                    worksheet.write(row_num+2, col_num, col,styles)
            # 保存
        workbook.save(book_name+'.xls')

    def copy2(self,wb):
        w = XLWTWriter()
        process(XLRDReader(wb, 'unknown.xls'), w)
        return w.output[0][1], w.style_list

    def main(self):
        self.read()
        book = self.getBookBySaleName("张三")
        # self.deal_with()
        self.myWrite(book,"张三")
if __name__ == '__main__':
    Transform().main()