import json

def load_knowledge():
    with open("data/knowledge_base.json", "r") as f:
        return json.load(f)

def get_answer(query):
    kb = load_knowledge()

    if "basic" in query.lower():
        return kb["pricing"]["basic"]

    if "pro" in query.lower():
        return kb["pricing"]["pro"]

    if "refund" in query.lower():
        return kb["policies"]["refund"]

    if "support" in query.lower():
        return kb["policies"]["support"]

    return "Sorry, I couldn't find that information."
