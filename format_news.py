import slaves as slave

news = slave.fetch_json("news.json")

for article in news:
    print("Titel:", article["title"])
    print("Zusammenfassung:", article["summary"])
    print("Quelle:", article["source"])
    print("-" * 50)