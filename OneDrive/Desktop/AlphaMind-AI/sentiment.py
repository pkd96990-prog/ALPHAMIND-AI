from transformers import pipeline


classifier = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert"
)


def analyze_sentiment(news):

    results = []

    for article in news:

        output = classifier(article)[0]

        results.append({
            "article": article,
            "sentiment": output["label"],
            "confidence": round(output["score"]*100,2)
        })

    return results