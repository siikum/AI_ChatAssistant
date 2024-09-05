from openai import OpenAI

# Function to get the assistant response
def get_assistant_response(user_message):
    client = OpenAI(
        api_key="sk-proj-IKtEhM3allMWMJNyZOHTT3BlbkFJynCBlBY16GWrXVDNBe2j",
    )
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Sikum Jr skilled in general tasks like Alexa and Google Cloud"},
            {"role": "user", "content": user_message}
        ]
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    while True:
        try:
            user_message = input("How can I help you mother?: ")
            if user_message.lower() == "quit":
                break
            else:
                assistant_response = get_assistant_response(user_message)
                print("Sikum Junior: ", assistant_response.strip("\n").strip())
        except Exception as e:
            print(f"Error: {e}")
