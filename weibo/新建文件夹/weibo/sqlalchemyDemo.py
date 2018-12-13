from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# 连接数据库，如果不存在则创建
engine = create_engine('sqlite:///H:/python/weibo/data.sqlite', echo=True)
Session = sessionmaker(bind=engine)

session = Session()
class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer)
    account_name = Column(String)
    comments_number = Column(Integer)
    like_number = Column(Integer)
    forwarding_time = Column(String)
    forwarded_number = Column(Integer)
    creative_type = Column(String)
    material_type = Column(String)
    def __repr__(self):
        return "<Data(id='%s', account_id='%s', account_name='%s')>" % (
                                self.id, self.account_id, self.account_name)
