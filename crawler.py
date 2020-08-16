# gets already saved entries
import feedparser
import datetime
import time
import urllib
import bs4 as bs
import urllib.request
import database


class NewsCrawler:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def crawl_feed(self):

        feed = feedparser.parse(self.url)

        # gets already saved entries
        saved_urls = database.get_saved_links(self.name)

        # saves current datetime in ISO8601 string format
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        # print(feed.entries)
        # iterates through all entries in the newsfeed and inserts new ones into the database
        for entry in feed.entries:
            if entry.link not in saved_urls:

                # source = urllib.request.urlopen(entry.link).read()
                # soup = bs.BeautifulSoup(source, "lxml")

                if self.name == "zeit":
                    # formats summary
                    if "</a>" in entry.summary:
                        a, summary = str(entry.summary).split("</a>", 1)
                    else:
                        summary = entry.summary

                    database.insert_data(
                        (
                            entry.link, #url
                            entry.title, #title
                            self.name, #newspaper
                            entry.author, #author
                            now, #scraped
                            "NULL", #isPremium
                            entry.category, #category
                            summary, #summary
                        )
                    )

                if self.name == "spiegel":
                    database.insert_data(
                        (
                            entry.link, #url
                            entry.title, #title
                            self.name, #newspaper
                            "NULL", #author
                            now, #scraped
                            "NULL", #isPremium
                            entry.category, #category
                            entry.summary, #summary
                        )
                    )

                if self.name == "welt":
                    database.insert_data(
                        (
                            entry.link, #url
                            entry.title, #title
                            self.name, #newspaper
                            "NULL", #author
                            now, #scraped
                            "NULL", #isPremium
                            entry.category, #category
                            entry.summary, #summary
                        )
                    )

                if self.name == "taz":
                    # formats summary
                    if "</a>" in entry.summary:
                        a, summary = str(entry.summary).split("</a>", 1)
                    else:
                        summary = entry.summary
                    database.insert_data(
                        (
                            entry.link, #url
                            entry.title, #title
                            self.name, #newspaper
                            entry.author, #author
                            now, #scraped
                            "NULL", #isPremium
                            "NULL", #category
                            summary, #summary
                        )
                    )

                if self.name == "nzz":
                    database.insert_data(
                        (
                            entry.link, #url
                            entry.title, #title
                            self.name, #newspaper
                            "NULL", #author
                            now, #scraped
                            "NULL", #isPremium
                            "NULL", #category
                            "NULL", #summary
                        )
                    )

                if self.name == "fr":
                    database.insert_data(
                        (
                            entry.link, #url
                            entry.title, #title
                            self.name, #newspaper
                            "NULL", #author
                            now, #scraped
                            "NULL", #isPremium
                            "NULL", #category
                            entry.summary, #summary
                        )
                    )

                if self.name == "nd":
                    database.insert_data(
                        (
                            entry.link, #url
                            entry.title, #title
                            self.name, #newspaper
                            "NULL", #author
                            now, #scraped
                            "NULL", #isPremium
                            entry.category, #category
                            "NULL", #summary
                        )
                    )

                if self.name == "sz":

                    soup = bs.BeautifulSoup(entry.summary, "lxml")
                    summary = soup.get_text()

                    database.insert_data(
                        (
                            entry.link, #url
                            entry.title, #title
                            self.name, #newspaper
                            "NULL", #author
                            now, #scraped
                            "NULL", #isPremium
                            entry.category, #category
                            summary, #summary
                        )
                    )