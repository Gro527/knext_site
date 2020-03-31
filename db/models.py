from knext_site.db import mappers
from knext_site.db.core import ss
from sqlalchemy.inspection import inspect
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import mapper
from sqlalchemy import desc
import hashlib
import logging


class Serializer(object):
    '''
    serialize to a jsoncodeable object
    '''
    def serialize(self):
        obj = {}
        for c in inspect(self).attrs.keys():
            data = getattr(self, c)
            if isinstance(data, (Serializer, list)):
                continue
            obj[c] = data

        return obj

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


class DataMixin(object):
    '''
    universal database functions
    '''
    @classmethod
    def get(cls, pk):
        return ss.query(cls).get(pk)


    @classmethod
    def delete_by_pk(cls, pk):
        return ss.query(cls).filter(cls.id==pk).delete()

    
    @classmethod
    def find_by(cls, name, value):
        if not hasattr(cls, name):
            raise Exception('unknown column: {}'.format(name))

        return ss.query(cls).filter(getattr(cls, name)==value).first()


    @classmethod
    def _query(cls, filters=[], order_by=None, offset=None, limit=None, join=None):
        if not isinstance(filters, list):
            filters = [filters]
        query = ss.query(cls).filter(*filters)
        if order_by is not None:
            query = query.order_by(order_by)
        if join is not None:
            query = query.join(join)
        if offset and limit:
            query = query.offset(offset).limit(limit)
        return query
    
    @classmethod
    def query(cls, filters=[], order_by=None, offset=None, limit=None, join=None):
        query = cls._query(filters, order_by, offset, limit, join)

        return query.all()


    @classmethod
    def count(cls, filters=[], order_by=None, offset=None, limit=None, join=None):
        query = cls.query(filters, order_by, offset, limit, join)

        return query.count()

    
    @classmethod
    def query_first(cls, filters=[]):
        query = cls._query(filters)
        return query.first()


    def delete(self):
        try:
            ss.delete(self)
            ss.commit()
        except SQLAlchemyError as e:
            logging.error("db action failed, error: {}".format(e.message))
            raise e
    

    def insert(self):
        try:
            ss.insert(self)
            ss.commit()
            ss.refresh(self)
        except SQLAlchemyError as e:
            logging.error("db action failed, error: {}".format(e.message))
            raise e


    def save(self):
        try:
            obj = ss.merge(self)
            ss.commit()
            if hasattr(obj, 'id') and not self.id:
                self.id = obj.id
            return obj
        except SQLAlchemyError as e:
            logging.error("db action failed, error: {}".format(e.message))
            raise e
        

class User(Serializer, DataMixin):
    def __init__(self, data):
        self.username = data.get('username')
        self.password = data.get('password')
        self.pw_sha1 = self.gen_sha1(self.password)

    def gen_sha1(self, password):
        encoder = hashlib.sha1()
        encoder.update(password)
        return encoder.hexdigest()

    @classmethod
    def get_by_username(cls, username):
        filters = []
        filters.append(User.username == username)

        users = cls.query(
            filters,
            order_by=desc(User.create_time)
        )
        if users:
            return users[0]
        return None
    
    @classmethod
    def login(cls, username, password):
        user = cls.get_by_username(username)
        if not user:
            print 111
            return None
        input_sha1 = user.gen_sha1(password)
        print input_sha1
        print user.pw_sha1
        if input_sha1 == user.pw_sha1:
            return user
        return None





mapper(User, mappers.User)

