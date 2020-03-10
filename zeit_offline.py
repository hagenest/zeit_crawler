import feedparser
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import os
import records


# reads in rss-feed
news_feed = feedparser.parse('http://newsfeed.zeit.de/all')

# reads in text file containing already saved links
saved_links = [line.rstrip('\n') for line in open('saved_links')]

# creates sql-database for saving metadata
database = records.Database()

#if not os.path.exists('/saved articels'):
    


# iterates over entries in news_feed
i = 0
for entries in news_feed.entries:

    # checks if entry is already in saved_links
    if not news_feed.entries[i]['link'] in saved_links:

        # adds url to saved_links file
        saved_links_file = open("saved_links", "a")
        saved_links_file.write(news_feed.entries[i]['link'] + "\n")
        saved_links_file.close

        # saves sites as html file
        url = news_feed.entries[i]['link']
        response = urllib.request.urlopen(url)
        new_file = open(news_feed.entries[i]['title'] + " " + news_feed.entries[i]['published'] + ".html", "wb")
        new_file.write(response.read())
        new_file.close

    i = i+1
    