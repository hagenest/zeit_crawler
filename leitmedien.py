import database as db
import crawler
import os


def crawl(crawler):
    for entry in crawler.feed.entries:
        print(entry.link)
        crawler.insert_data(entry.link)


def main():
    zeitCrawler = crawler.Zeit("http://newsfeed.zeit.de/all", "Zeit Online")
    crawl(zeitCrawler)


if __name__ == "__main__":
    main()
