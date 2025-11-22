analyze_sentiment(message):
    message = message.lower()
    if "stress" in message or "overwhelm" in message:
        return "stress"
    if "sad" in message or "upset" in message:
        return "sad"
    if "tired" in message or "low" in message:
        return "low-energy"
    if "happy" in message or "good" in message:
        return "positive"
    return "neutral"

