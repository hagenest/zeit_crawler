from peewee import *
import datetime


db = SqliteDatabase("leitmedien.db", pragmas={"foreign_keys": 1})


class BaseModel(Model):
    class Meta:
        database = db


class Article(BaseModel):

    url = TextField(primary_key=True)
    title = TextField()
    site = TextField()
    date = DateField(default=datetime.datetime.now)
    isPremium = BooleanField()
    summary = TextField()


class Keyword(BaseModel):
    article = ForeignKeyField(Article, backref="keywords")
    ykeyword = TextField()


class Author(BaseModel):
    article = ForeignKeyField(Article, backref="authors")
    author = TextField()


db.connect()
db.create_tables([Article, Keyword, Author])