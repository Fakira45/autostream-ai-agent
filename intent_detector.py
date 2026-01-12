def detect_intent(user_input: str):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"

    if any(word in user_input for word in ["price", "pricing", "cost", "plan"]):
        return "pricing"

    if any(word in user_input for word in ["sign up", "buy", "subscribe", "try", "pro plan"]):
        return "high_intent"

    return "unknown"
