from typing import TypedDict
from langgraph.graph import StateGraph, END

from agent.intent_detector import detect_intent
from agent.rag import get_answer
from agent.tools import mock_lead_capture


class AgentState(TypedDict):
    user_input: str
    intent: str
    name: str
    email: str
    platform: str


def intent_node(state: AgentState):
    state["intent"] = detect_intent(state["user_input"])
    return state


def response_node(state: AgentState):
    intent = state["intent"]

    if intent == "greeting":
        print("Agent: Hi 👋 I’m AutoStream AI. How can I help you?")
        return state

    if intent == "pricing":
        pro = get_answer("pro")
        print(f"""Agent:
  Pro Plan
- Price: {pro['price']}
- Videos: {pro['videos']}
- Resolution: {pro['resolution']}
- Features: {', '.join(pro['features'])}
""")
        return state

    if intent == "high_intent":
        if not state.get("name"):
            state["name"] = input("Agent: Your name? ")
        if not state.get("email"):
            state["email"] = input("Agent: Your email? ")
        if not state.get("platform"):
            state["platform"] = input("Agent: Creator platform? ")

        mock_lead_capture(
            state["name"], state["email"], state["platform"]
        )
        return state

    return state


graph = StateGraph(AgentState)

graph.add_node("intent", intent_node)
graph.add_node("response", response_node)

graph.set_entry_point("intent")
graph.add_edge("intent", "response")
graph.add_edge("response", END)

app = graph.compile()

while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break
    app.invoke({"user_input": msg})
