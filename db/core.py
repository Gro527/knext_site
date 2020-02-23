from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy.ext.declarative import declarative_base
pymysql.install_as_MySQLdb()


engine = create_engine('mysql+mysqldb://root:root@localhost:3306/knext')

SqlSession = sessionmaker(bind=engine)
ss = SqlSession()
base = declarative_base()
metadata = base.metadata

def init_db():
    base.metadata.create_all(engine)