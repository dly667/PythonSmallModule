import pandas as pd
import xlrd,xlwt
import xlsxwriter
from xlutils.filter import process, XLRDReader, XLWTWriter
Source_FileName = "数据格式表.xlsx"
First_SheetName = "交易月综合表"
class Separ(object):
    def __init__(self,filename):
        self.filename=filename
        self.salenames = None
        pass
    # pandas 获取数据列表
    def getData(self):
        book_list = dict()
        source_data = pd.ExcelFile(self.filename)
        for sn in source_data.sheet_names:
            temp = list()
            df = source_data.parse(sn, skiprows=1, skipfooter=1)
            if sn == First_SheetName:
                self.salenames = df.groupby(by=df['所属销售']).size().index

            for salename in self.salenames:
                zs = df[df["所属销售"] == salename]
                # temp.append(zs)
                if (salename in book_list.keys()) == False:

                    book_list[salename] = []
                book_list[salename].append({sn:zs})


        return book_list

    def wrt(self,book_list):
        # 创建一个workbook 设置编码
        for salename in book_list:
            # 打开一个xlsx文件
            workbook = xlsxwriter.Workbook(salename + '.xlsx')

            # 自定义样式
            cell_format1 = workbook.add_format()
            cell_format1.set_num_format('mmm-yy')

            # 时间格式
            cell_format2 = workbook.add_format()
            cell_format2.set_num_format('yyyy/m/d')
            # 百分号小数点格式
            cell_format3 = workbook.add_format()
            cell_format3.set_num_format(0x0a)

            # 首行样式 加粗
            cell_format = workbook.add_format()
            cell_format.set_bold(True)
            for sheet in book_list[salename]:

                for item in sheet:

                    # 创建一个worksheet
                    worksheet = workbook.add_worksheet(item)
                    #设置 列的宽度
                    worksheet.set_column("A:A", 15)  # Column  E   width set to 20.
                    worksheet.set_column("N:N", 10)  # Column  E   width set to 20.
                    worksheet.set_column("C:C", 10)  # Column  E   width set to 20.
                    worksheet.set_column("O:O", 10)  # Column  E   width set to 20.
                    rows, cols = sheet[item].shape
                    for row in range(0, rows):
                        for col in range(0, cols):

                            if row == 1:
                                # first_styles = getStyle1(workbook, sn_0, 1, col)
                                worksheet.write(row, col, (sheet[item].columns[col]),cell_format)

                            # 第一张子表与其他子表不同
                            if item == First_SheetName:

                                if col in [0, 3, 4, 6, 7, 8, 10]:
                                    print(sheet[item].iloc[row, col])

                                    worksheet.write(row + 2, col, sheet[item].iloc[row, col])
                                elif col == 1:

                                    worksheet.write(row + 2, col, (sheet[item].iloc[row, col]))
                                elif col == 2:

                                    worksheet.write(row + 2, col, (sheet[item].iloc[row, col]),cell_format1)
                                elif col in [5, 9, 11]:
                                    worksheet.write(row + 2, col, (sheet[item].iloc[row, col]),cell_format3)
                                else:
                                    worksheet.write(row + 2, col, (sheet[item].iloc[row, col]),cell_format2)
                            else:
                                if col == 2:

                                    worksheet.write(row + 2, col, (sheet[item].iloc[row, col]),cell_format2)
                                elif col in [6,7]:
                                    worksheet.write(row + 2, col, int(sheet[item].iloc[row, col]))
                                elif col in [5, 8,10,12]:
                                    worksheet.write(row + 2, col, int(sheet[item].iloc[row, col]),cell_format3)
                                else:
                                    worksheet.write(row + 2, col, sheet[item].iloc[row, col])

            #关闭并保存
            workbook.close()

    def main(self):
        data_list = self.getData()
        self.wrt(data_list)
        pass

if __name__ == '__main__':
    Separ(Source_FileName).main()