def format_articles(entries):
    """RSSの記事一覧から、タイトルとURLだけを取り出す。"""
    articles = []

    for entry in entries:
        article = {
            "title": entry.get("title", "タイトルなし"),
            "url": entry.get("link", "")
        }
        articles.append(article)

    return articles
