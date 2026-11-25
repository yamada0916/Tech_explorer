import feedparser

url = "https://zenn.dev/feed"
feed = feedparser.parse(url)

for article in feed.entries:
    print("タイトル：" + article.title)
    print("URL：" + article.link)
