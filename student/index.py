#
# import matplotlib.pyplot as plt
# import matplotlib
# #指定默认字体
# # matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# zhfont1 = matplotlib.font_manager.FontProperties(fname='./simhei.ttf')
# # matplotlib.rcParams['font.family']='simhei'
# #解决负号'-'显示为方块的问题
# matplotlib.rcParams['axes.unicode_minus'] = False
# with open('inform.txt', 'r') as f:
#     file_content=f.read().split('\n')
# table_header = file_content[0].split('\t ')
# student_list = file_content[1:]
#
# name_list = table_header
# num_list = [52.4, 57.8, 59.1, 54.6]
# rects=plt.bar(range(len(num_list)), num_list, color='rgby')
# # X轴标题
# index=[0,1,2,3]
# index=[float(c)+0.4 for c in index]
# plt.ylim(ymax=100, ymin=0)
# plt.xticks(index, name_list,fontproperties=zhfont1)
# plt.ylabel("分数(score)",fontproperties=zhfont1) #X轴标签
# for rect in rects:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width() / 2, height, str(height)+'%', ha='center', va='bottom')
# plt.show()
import matplotlib.pyplot as plt
import matplotlib
import numpy as np



class Student:
    def getSourceData(self):
        with open('inform.txt', 'r') as f:
            file_content =f.read().split('\n')

            student_list = file_content[1:]
            final_dic = {}
            for item in student_list:
                final_dic[item.split()[0]] = item.split()[3]
        return final_dic
    def draw(self):
        data = Student().getSourceData()
        # Fixing random state for reproducibility
        np.random.seed(19680801)
        zhfont = matplotlib.font_manager.FontProperties(fname='./simhei.ttf')

        plt.rcdefaults()
        fig, ax = plt.subplots()

        # Example data
        people = data.keys()
        y_pos = np.arange(len(people))
        # performance = 3 + 10 * np.random.rand(len(people))

        performance = list(data.values())
        error = np.random.rand(len(people))

        ax.barh(y_pos, performance, xerr=error, align='center',
                color='gray', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(people,fontproperties=zhfont)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('分数', fontproperties=zhfont)
        ax.set_title('学生分数直方图', fontproperties=zhfont)

        plt.show()
    def aa(self,num,data):
        return data.values()[num]

if  __name__ == '__main__':
    print(Student().draw())