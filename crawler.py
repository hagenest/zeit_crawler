from bs4 import BeautifulSoup as bs
import re
import requests
import feedparser
import database as db


class Crawler:
    def __init__(self, feed, site):
        self.feed = feedparser.parse(feed)
        self.site = site

    # returns urls that arent't already in the database from given rss-feed
    def get_new_urls(self):
        urlList = []
        saved_urls = db.Article.select("url").get()
        for entry in self.feed.entries:
            if entry.link not in saved_urls:
                urlList.append(entry.link)
        return urlList

    def generate_soup(self, url):
        content = requests.get(url).content
        soup = bs(content, "lxml")
        return soup

    def get_title(self, soup):
        return soup.title.string

    def get_summary(self, soup):
        return soup.find(name="description")

    def get_keywords(self, soup):
        keywords = soup.find(name="keywords")
        return keywords.split(", ")

    def get_isPremium(self, soup):
        return "NULL"

    def get_authors(self, soup):
        authors = soup.find(name="author")
        return authors.split(", ")

    def insert_data(
        self, url  # , title, site, date, isPremium, summary, keywords, authors
    ):
        soup = self.generate_soup(url)
        db.Article(
            url=url,
            title=self.get_title(soup),
            site=self.site,
            isPremium=self.get_isPremium(soup),
            summary=self.get_summary(soup),
        ).save()
        for keyword in self.get_keywords:
            db.Keyword(url = url, keyword=self.get_keywords(soup)).save()
        for author in self.get_authors:
            db.Author(url = url, author=self.get_authors(soup)).save()


class Zeit(Crawler):
    
    def get_isPremium(self, soup):
        if "Exklusiv für Abonnenten" in soup.prettify():
            return True
        else:
            return False
