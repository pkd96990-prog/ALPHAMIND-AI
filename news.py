import feedparser


def get_news(company):

    url = f"https://news.google.com/rss/search?q={company}+stock"

    feed = feedparser.parse(url)

    articles = []

    for item in feed.entries[:10]:
        articles.append(item.title)

    return articles