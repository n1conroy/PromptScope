def analyze_tokens(text: str):
    tokens = text.split()
    return [{"token": token, "length": len(token)} for token in tokens]
