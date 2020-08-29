# crawls through news sites via their rss-feeds

import feedparser
import datetime
import time
import urllib
import bs4 as bs
import urllib.request
import database as db
import requests


class NewsCrawler:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def crawl_feed(self):

        # parses rss-feed through feedparser library
        feed = feedparser.parse(self.url)

        print(feed)

        # gets already saved entries
        saved_urls = db.get_saved_links(self.name)

        # saves current datetime in shortened ISO8601 string format
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        # iterates through all entries in the newsfeed and inserts new ones into the db
        for entry in feed.entries:
            if entry.link not in saved_urls:

                # checks for each sites' specific quirks; I'd love a less ugly solution
                if self.name == "zeit":
                    # formats summary
                    if "</a>" in entry.summary:
                        a, summary = str(entry.summary).split("</a>", 1)
                    else:
                        summary = entry.summary

                    db.insert_data(
                        (
                            entry.link,  # url
                            entry.title,  # title
                            self.name,  # newspaper
                            entry.author,  # author
                            now,  # scraped
                            "NULL",  # isPremium
                            entry.category,  # category
                            summary,  # summary
                        )
                    )

                if self.name == "spiegel":
                    req = requests.get(entry.link)
                    soup = bs.BeautifulSoup(req.text, "html.parser")
                    author = soup.find("meta", "author")
                    db.insert_data(
                        (
                            entry.link,  # url
                            entry.title,  # title
                            self.name,  # newspaper
                            author,  # author
                            now,  # scraped
                            "NULL",  # isPremium
                            entry.category,  # category
                            entry.summary,  # summary
                        )
                    )

                if self.name == "welt":
                    req = requests.get(entry.link)
                    soup = bs.BeautifulSoup(req.text, "html.parser")
                    author = soup.find(name="author")
                    db.insert_data(
                        (
                            entry.link,  # url
                            entry.title,  # title
                            self.name,  # newspaper
                            author,  # author
                            now,  # scraped
                            "NULL",  # isPremium
                            entry.category,  # category
                            entry.summary,  # summary
                        )
                    )

                if self.name == "taz":
                    # formats summary
                    if "</a>" in entry.summary:
                        a, summary = str(entry.summary).split("</a>", 1)
                    else:
                        summary = entry.summary
                    db.insert_data(
                        (
                            entry.link,  # url
                            entry.title,  # title
                            self.name,  # newspaper
                            entry.author,  # author
                            now,  # scraped
                            "NULL",  # isPremium
                            "NULL",  # category
                            summary,  # summary
                        )
                    )

                if self.name == "nzz":
                    req = requests.get(entry.link)
                    soup = bs.BeautifulSoup(req.text, "html.parser")
                    author = soup.find(name="author")
                    db.insert_data(
                        (
                            entry.link,  # url
                            entry.title,  # title
                            self.name,  # newspaper
                            author,  # author
                            now,  # scraped
                            "NULL",  # isPremium
                            "NULL",  # category
                            "NULL",  # summary
                        )
                    )

                if self.name == "fr":
                    req = requests.get(entry.link)
                    soup = bs.BeautifulSoup(req.text, "html.parser")
                    author = soup.find(name="author")
                    db.insert_data(
                        (
                            entry.link,  # url
                            entry.title,  # title
                            self.name,  # newspaper
                            author,  # author
                            now,  # scraped
                            "NULL",  # isPremium
                            "NULL",  # category
                            entry.summary,  # summary
                        )
                    )

                if self.name == "nd":
                    req = requests.get(entry.link)
                    soup = bs.BeautifulSoup(req.text, "html.parser")
                    author = soup.find(name="author")
                    db.insert_data(
                        (
                            entry.link,  # url
                            entry.title,  # title
                            self.name,  # newspaper
                            author,  # author
                            now,  # scraped
                            "NULL",  # isPremium
                            entry.category,  # category
                            "NULL",  # summary
                        )
                    )

                if self.name == "sz":

                    soups = bs.BeautifulSoup(entry.summary, "lxml")
                    summary = soups.get_text()

                    req = requests.get(entry.link)
                    soup = bs.BeautifulSoup(req.text, "html.parser")
                    author = soup.find(name="author")

                    db.insert_data(
                        (
                            entry.link,  # url
                            entry.title,  # title
                            self.name,  # newspaper
                            author,  # author
                            now,  # scraped
                            "NULL",  # isPremium
                            entry.category,  # category
                            summary,  # summary
                        )
                    )

    # uses bs4 to get specific info out of html page
    # failcase if the information isn't available in the rss-feed
    def get_bs(self, term):
        req = requests.get(self.link)
        soup = bs.BeautifulSoup(req.text, "html.parser")
        return soup.find(name=term)
