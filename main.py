from agent.agent import AutoStreamAgent

agent = AutoStreamAgent()

print("🤖 AutoStream AI Agent (type 'exit' to quit)\n")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    response = agent.chat(user)
    print("Agent:", response)
