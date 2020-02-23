from knext_site.db.core import ss, init_db, base, metadata
from sqlalchemy import Table, Integer, Column, String, DateTime, ForeignKey, UniqueConstraint, Index, Float, Enum, Date
from sqlalchemy.schema import Sequence
from datetime import datetime


# class iUser(base):
#     __tablename__ = 'user'
#     id = Column(Integer,
#                Sequence('user_id_seq', start=1001, increment=1),
#                primary_key = True)
#     username = Column(String(64))
#     pw_sha1 = Column(String(256))
    

User = Table('user', metadata, 
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('username', String(64), nullable=False),
            Column('pw_sha1', String(256), nullable=False),
            
            # auto fields
            Column('create_time', DateTime, default=datetime.now),
            Column('modify_time', DateTime, default=datetime.now)
            )

init_db()