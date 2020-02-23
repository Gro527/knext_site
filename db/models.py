from knext_site.db.mappers import iUser
from knext_site.db.core import ss
from sqlalchemy import _or
from sqlalchemy.inspection import inspect
from sqlalchemy.exc import SQLAlchemyError
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
        ss.query(cls).filter(*filters)
        if order_by is not None:
            query = query.order_by(order_by)
        if join is not None:
            query = query.join(join)
        if offset and limit:
            query = query.offset(offset).limit(limit)
    
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
    def __init__(self, input):
        self.username = input.get('username')
        self.password = input.get('password')

    def gen_sha1(self, password):
        return hashlib.sha1(password)

