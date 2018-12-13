import xlrd
import xlwt
from xlutils.filter import process, XLRDReader, XLWTWriter
from sqlalchemyDemo import session,Data
data = [
    1288915263,2611704935,2778292197,3427645762,2125939111,2417139911,
    2388955087,2594986464,2542011901,2418724427,2518353303,2208751963,
    2590506110,1905391435,2590508324,2590506210,2305490713,2590506142,
    2590506130,5556545776,5105430040,1710175603,5551535898,5575615685,
    1797168385,3745736194,3508612897,3927469685,2566267767,5181462351,
    5295768846,3820915614,3959178104,3957042973,3949956132,3956862160,
    1916657595,3312977743,2540937243,3819226943,3928511449,1683322745,
    2540225721,2516831703,2050142347,3506774562,6195217648,2270603713,
    6179234995,3933794230,6174430563,6396740795,2590506090,3453751692,
    1507156867,2649761871,1960060805,3980980810,1044825203,2158074297,
    2676362053,3789154482,1936009361,2028845887,5085042263,2130830185,
    2037181057,2611712133,1908516792,5780949476,5071610242,2061911495
]

class SplitData(object):
    # 通过条件得到数据
    def getData(self,condition):

        data = session.query(Data).filter(Data.account_id == '2061911495').all()
        return data
    # 将数据整理好
    def deal_with(self,gory_data):
        id = Column(Integer, primary_key=True)
        account_id = Column(Integer)
        account_name = Column(String)
        comments_number = Column(Integer)
        like_number = Column(Integer)
        forwarding_time = Column(String)
        forwarded_number = Column(Integer)
        creative_type = Column(String)
        material_type = Column(String)
        followers_count = Column(Integer)
        follow_count = Column(Integer)
        forward_sum_count = Column(Integer)
        unix_time = Column(Integer)
        # 1. 设置表头
        table_header = [id,account_id,account_name,comments_number,]
        for gd in gory_data:
            print(gd.id)
    # 写入到excel表格
    def write_to(self):
        pass
    def main(self):
        gory_data = self.getData('1288915263')
        self.deal_with(gory_data)



if __name__ == '__main__':
    SplitData().main()