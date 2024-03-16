import pandas as pd
from gnews import NewsClient


lang = "fr"

nb_articles = 100


client = NewsClient(lang=lang)

choix = input("Voulez-vous des actualités Top du moment (1) ou des actualités en rapport avec un mot-clé (2) ? ")

if choix == "1":
    articles = client.get_top_news(max_results=100)

elif choix == "2":
    keyword = input("Entrez votre mot-clé : ")
    articles = client.get_news(keyword, max_results=100)
else:
    print("Choix invalide.")
    exit()

df = pd.DataFrame({
    "Titre": [article.title for article in articles],
    "Lien": [article.url for article in articles],
    "Date de publication": [article.publish_date for article in articles],
    "Source": [article.source for article in articles],
    "Résumé": [article.summary for article in articles]
})

df.to_csv("news.csv", index=False)

