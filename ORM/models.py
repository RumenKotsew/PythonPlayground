import sqlite3

from base import Metabase
from queries import create_table, insert, drop, select_query
from collections import OrderedDict


class BaseModel(metaclass=Metabase):

    db = sqlite3.connect("db.sqlite3")
    db.row_factory = sqlite3.Row
    c = db.cursor()

    __tablename__ = None

    @classmethod
    def drop_tables(cls):
        for reg in list(cls._registry):
            BaseModel.c.execute(drop(reg))
        BaseModel.db.commit()

    @classmethod
    def create_all_tables(cls):
        BaseModel.drop_tables()
        for reg in list(cls._registry):
            BaseModel.c.execute(create_table(reg))
        BaseModel.db.commit()

    @classmethod
    def create_obj(cls, *args, **kwargs):
        print(insert(cls, *args, **kwargs))
        attrs = tuple([kwargs[key] for key in kwargs])
        BaseModel.c.execute(insert(cls, *args, **kwargs), attrs)
        BaseModel.db.commit()

    @classmethod
    def filter(cls, **kwargs):
        obj = BaseModel.c.execute(select_query(cls, list(kwargs.keys())[0],
                                               list(kwargs.values())[0])) \
                                  .fetchone()
        attrs = OrderedDict()
        for key, value in dict(obj).items():
            attrs[key] = value
        return dict(attrs)
