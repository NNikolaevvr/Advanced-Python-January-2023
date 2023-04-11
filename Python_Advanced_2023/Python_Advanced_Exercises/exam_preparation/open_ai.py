import openai

openai.api_key = "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"


def ask_chatGPT(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response["choices"][0]["text"]
    parts = message.split("\n")
    code = False
    for part in parts:
        if part.startswith("```"):
            code = not code
            print(part)
        elif code:
            print("    " + part)
        else:
            print(part)


while True:
    question = input("You: ")
    if question == "exit":
        break
    print("ChatGPT:")
    ask_chatGPT(question)
    print("\n")