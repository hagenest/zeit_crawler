from peewee import *
import datetime


# Create a peewee database instance
db = SqliteDatabase("leitmedien.db", pragmas={"foreign_keys": 1})


# Define a base model class that specifies which database to use.
class BaseModel(Model):
    class Meta:
        database = db


# Define database table for articles
class Article(BaseModel):

    url = TextField(primary_key=True)
    title = TextField()
    site = TextField()
    date = DateField(default=datetime.datetime.now)
    isPremium = BooleanField()
    summary = TextField()


# Define database table for keywords
class Keyword(BaseModel):
    article = ForeignKeyField(Article, backref="keywords")
    ykeyword = TextField()

# Define database table for authors
class Author(BaseModel):
    article = ForeignKeyField(Article, backref="authors")
    author = TextField()


def setup_database():
    db.connect()
    db.create_tables([Article, Keyword, Author])
    db.close()


if __name__ == "__main__":
    setup_database()