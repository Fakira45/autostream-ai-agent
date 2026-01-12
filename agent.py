from agent.intent_detector import detect_intent
from agent.rag import get_answer
from agent.tools import mock_lead_capture

class AutoStreamAgent:
    def __init__(self):
        self.state = {
            "name": None,
            "email": None,
            "platform": None
        }

    def chat(self, user_input):
        intent = detect_intent(user_input)

        if intent == "greeting":
            return "Hi 👋 I’m AutoStream AI. How can I help you today?"

        if intent == "pricing":
            pro = get_answer("pro")
            return (
                f"💼 Pro Plan:\n"
                f"- Price: {pro['price']}\n"
                f"- Videos: {pro['videos']}\n"
                f"- Resolution: {pro['resolution']}\n"
                f"- Features: {', '.join(pro['features'])}"
            )

        if intent == "high_intent":
            if not self.state["name"]:
                return "Great! 😊 May I know your name?"

        if self.state["name"] is None:
            self.state["name"] = user_input
            return "Thanks! Please share your email."

        if self.state["email"] is None:
            self.state["email"] = user_input
            return "Which platform do you create content on? (YouTube / Instagram)"

        if self.state["platform"] is None:
            self.state["platform"] = user_input
            mock_lead_capture(
                self.state["name"],
                self.state["email"],
                self.state["platform"]
            )
            return "🎉 You’re all set! Our team will contact you soon."

        return "How else can I help you?"
