import zeit_database
import feedparser
import os.path
import datetime
import time
import urllib


# reads in rss-feed
newsfeed = feedparser.parse("http://newsfeed.zeit.de/all")

# creates a new database if there isn't one already
if not os.path.isfile("zeit.db"):
    zeit_database.create_database(is_debug_mode=False)

# gets already saved entries
saved_links = zeit_database.get_saved_links()

# saves current datetime
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# iterates through all entries in the newsfeed and inserts new ones into the database
for entry in newsfeed.entries:
    if entry.link not in saved_links:
        zeit_database.insert_data(
            (
                entry.link,
                entry.title,
                entry.author,
                now,
                time.strftime("%Y-%m-%d %H:%M", entry.published_parsed),
                "NULL",
                entry.tags[0].term,
                entry.summary,
                entry.title + ".txt",
            )
        )

        # saves article as html in the articles folder
        # response = urllib.request.urlopen(entry.link)
        # new_file = open("/articles/" + entry.title.replace('.','') + ".html", "wb")
        # new_file.write(response.read())
        # new_file.close()
