import xlrd
from xlutils.filter import process, XLRDReader, XLWTWriter
def copy2(wb):
    w = XLWTWriter()
    process(XLRDReader(wb, 'unknown.xls'), w)
    return w.output[0][1], w.style_list

rb = xlrd.open_workbook('1.xls', formatting_info=True, on_demand=True)
wb, s = copy2(rb)
wbs = wb.get_sheet(0)
rbs = rb.get_sheet(0)
styles = s[rbs.cell_xf_index(0, 1)]
rb.release_resources()  #关闭模板文件

# wbs.write(0, 1, '43340', styles)
wb.save("2.xls")