import openai

openai.api_key = "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"

query_prompt = input("enter a question: ")

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=query_prompt,
    max_tokens=100
)
print(response.choices[0].text.strip())

# The above code is a simple example of how to use the OpenAI API to generate text.