from sqlalchemy import create_engine
from  sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy import Column,String ,Integer,Date,DateTime
engin=create_engine('mysql://root:puhao@localhost:3306/shiyanlou?charset=utf8')
Base=declarative_base()
class Course(Base):
    __tablename__='courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    description = Column(String(1024))
    type = Column(String(64), index=True)
    students = Column(Integer)
    a=Column(Date)
    def __repr__(self):
        return 'name is %s' %self.name
class Cangku(Base):
    __tablename__='repositories'
    id=Column(Integer,primary_key=True)
    name=Column(String(64))
    update_time=Column(DateTime)
class MyClass(Base):
    __tablename__='classdata'
    id=Column(Integer,primary_key=True)
    name=Column(String(100))
    author=Column(String(100))

#如果不存到数据库，可以不用创建这些
if __name__ == '__main__':
    Base.metadata.create_all(engin)

