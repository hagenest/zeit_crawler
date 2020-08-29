# main script, which calls all other packages

import crawler
import database as db
import os.path


# array of newspapers to scrape
newspapers = [
    ["http://newsfeed.zeit.de/all", "zeit"],
    ["https://www.spiegel.de/schlagzeilen/index.rss", "spiegel"],
    ["https://www.welt.de/feeds/latest.rss", "welt"],
    ["https://taz.de/!s=&ExportStatus=Intern&SuchRahmen=Online;rss/", "taz"],
    ["https://www.nzz.ch/recent.rss", "nzz"],
    ["https://www.fr.de/rssfeed.rdf", "fr"],
    ["https://www.neues-deutschland.de/rss/aktuell.php", "nd"],
    ["https://rss.sueddeutsche.de/app/service/rss/alles/index.rss?output=rss", "sz"],
]


def main():
    # creates a new db if there isn't one already
    if not os.path.isfile("leitmedien.db"):
        db.create_table()

    for entry in newspapers:
        news_crawler = crawler.NewsCrawler(name=entry[1], url=entry[0])
        news_crawler.crawl_feed()


if __name__ == "__main__":
    main()
