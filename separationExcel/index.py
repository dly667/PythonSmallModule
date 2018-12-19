import pandas as pd
import xlrd,xlwt
from xlutils.filter import process, XLRDReader, XLWTWriter
filename="数据格式表.xls"


data=pd.ExcelFile(filename)
sn_0=data.sheet_names[0]
sn_1=data.sheet_names[1]
df_0=data.parse(sn_0,skiprows=1,skipfooter=1)
df_1=data.parse(sn_1,skiprows=1,skipfooter=1)


salename=df_0.groupby(by=df_0['所属销售']).size().index
zs_0_name=salename[0]
zs_0=df_0[df_0["所属销售"]==zs_0_name]
zs_1=df_1[df_1["所属销售"]==zs_0_name]
print(zs_0)

workbook = xlrd.open_workbook(u'数据格式表.xls', formatting_info=True, on_demand=True)

wt_workbook = xlwt.Workbook(encoding='utf-8')
worksheet = wt_workbook.add_sheet(sn_0,cell_overwrite_ok=True)


# wb = w.output[0][1]
# wbs = wb.get_sheet(0)
# wbs.write(1, 1, 11, styles)


def getStyle1(workbook,sheet,t1,t2):
    w = XLWTWriter()
    process(XLRDReader(workbook, 'unknown.xls'), w)
    s = w.style_list
    xl_sheet1 = workbook.sheet_by_name(sheet)

    styles = s[xl_sheet1.cell_xf_index(t1, t2)]
    return  styles

rows,cols = zs_0.shape
for row in range(0,rows):
    for col in range(0,cols):
        styles = getStyle1(workbook, sn_0, 2, col)
        if row == 1:
            first_styles = getStyle1(workbook, sn_0, 1, col)
            worksheet.write(row , col, (zs_0.columns[col]),first_styles)
        # print(zs_0.iloc[row, col])
        if col in [0,3,4,6,7,8,10]:
            worksheet.col(col).width = 4333
            worksheet.write(row+2, col, int(zs_0.iloc[row, col]), styles)
        elif col == 1:

            worksheet.write(row+2, col, str(zs_0.iloc[row, col]), styles)
        elif col == 2:

            worksheet.write(row+2, col, (zs_0.iloc[row, col]), styles)
        elif col in [5,9,11]:
            worksheet.write(row+2, col, float(zs_0.iloc[row, col]), styles)
        else:
            dateFormat = xlwt.XFStyle()

            styles.num_format_str = 'yyyy/m/d'

            worksheet.col(col).width = 4333
            worksheet.write(row+2, col, (zs_0.iloc[row, col]), styles)


c
