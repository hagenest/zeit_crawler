import feedparser
import urllib.request, urllib.error, urllib.parse


# reads in rss-feed
news_feed = feedparser.parse('http://newsfeed.zeit.de/all')

# reads in text file containing already saved links
saved_links = [line.rstrip('\n') for line in open("saved_links")]


# iterates over entries in news_feed
i = 0
for entries in news_feed.entries:
    if not news_feed.entries[i]['link'] in saved_links:

        # adds url to saved_links file
        f = open("saved_links", "a")
        f.write(news_feed.entries[i]['link'] + "\n")
        f.close

        # saves sites as html file
        url = news_feed.entries[i]['link']
        response = urllib.request.urlopen(url)
        web_content = response.read()
        f = open(news_feed.entries[i]['title'] + " " + news_feed.entries[i]['published'] + ".html", "wb")
        f.write(web_content)
        f.close
    i = i+1
