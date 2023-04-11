import openai

# Apply the API key
openai.api_key = "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"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

def check_for_greeting(response):
    greetings = ["hello", "hi", "hey", "howdy", "hola", "wassup"]
    for greeting in greetings:
        if greeting in response.lower():
            return True
    return False

def check_for_farewell(response):
    farewells = ["bye", "goodbye", "later", "peace out", "adios"]
    for farewell in farewells:
        if farewell in response.lower():
            return True
    return False

while True:
    prompt = input("You: ")
    if prompt == "quit":
        break
    response = generate_response(prompt)
    if check_for_greeting(prompt):
        response = "Hello! How can I help you today?"
    elif check_for_farewell(prompt):
        response = "Goodbye! Have a great day."
    print("ChatGPT: " + response)
