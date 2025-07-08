from textblob import TextBlob

print("Enter a sentence and I’ll analyze its sentiment:")

while True:
    text = input("👉 Your text (or type 'exit'): ")
    if text.lower() == 'exit':
        break

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # -1 to 1

    if polarity > 0:
        print("🟢 Sentiment: Positive 😊")
    elif polarity < 0:
        print("🔴 Sentiment: Negative 😠")
    else:
        print("🟡 Sentiment: Neutral 😐")
