import database as db
import crawler
import os


if __name__ == "__main__":
    db.db.create_tables(["Article", "Keyword", "Author"])

    zeit = crawler.Zeit("http://newsfeed.zeit.de/all", "Die Zeit")
    for entry in zeit.feed.entries:
        zeit.insert_data(entry.link)
