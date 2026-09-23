from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0.3
)

print("AI Factory Copilot LLM started!")
print("Type 'exit' to stop.\n")

while True:
    question = input("Operator: ")

    if question.lower() == "exit":
        break

    response = llm.invoke(question)

    print("\nAI Assistant:")
    print(response.content)
    print()