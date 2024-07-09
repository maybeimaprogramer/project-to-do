from sqlalchemy.orm import DeclarativeBase,Mapped,sessionmaker,relationship,mapped_column
from sqlalchemy import Column,Integer,String,ForeignKey,Boolean,DateTime,Float,Date,Text
from sqlalchemy import Engine,create_engine
from dotenv import load_dotenv
import os


class Base(DeclarativeBase):
    pass





class User(Base):
    __tablename__ = 'users'
    userid:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    username:Mapped[str]=mapped_column(String(20),nullable=False,unique=True)
    password:Mapped[str]=mapped_column(String(255),nullable=False)
    firstname:Mapped[str]=mapped_column(String(20),nullable=False)
    lastname:Mapped[str]=mapped_column(String(20),nullable=False)
    task:Mapped["Tasks"]=relationship(backref="tasks",passive_deletes=True)







class Tasks(Base):
    __tablename__ = 'tasks'
    taskid:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    taskname:Mapped[str]=mapped_column(String(20),nullable=False)
    taskdescription:Mapped[str]=mapped_column(String(100),nullable=False)
    userid:Mapped[int]=mapped_column(ForeignKey("users.userid",ondelete="cascade"))




load_dotenv()
databaseconnection = os.getenv("databaseconnection")
print(databaseconnection)
engine:Engine=create_engine(databaseconnection)
global localsession;
localsession=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base.metadata.create_all(bind=engine)


    