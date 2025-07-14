from textblob import TextBlob

def get_sentiment(text: str):
    blob = TextBlob(text)
    return {
        "polarity": blob.polarity,
        "subjectivity": blob.subjectivity
    }
