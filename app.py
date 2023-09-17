import openai

with open('key.txt', 'r') as file:
    openai.api_key = file.read().strip()

def get_reply(name, age, user_input, date_input):
    response = openai.Completion.create(
        engine = "davinci",
        prompt = f"{name}, a {age}-year-old individual, is on a date. Their date mentioned: '{date_input}'. In response, {name} said: '{user_input}'. Given this context, provide a clear and concise reply in elgish to what would be an appropriate and thoughtful reply for {name}'s date?",
        max_tokens = 50
    )

    return response.choices[0].text.strip()


def main():
    name = input("Enter your first name: ")
    age = input("Enter your age: ")

    while True:
        user_input = input("What did you say to your date? (Exit anytime by replying 'exit'): ")
        if user_input == 'exit':
            break

        date_input = input("What your date say to you? (Exit anytime by replying 'exit'): ")
        if user_input == 'exit':
            break


        gptReponse = get_reply(name,age,user_input, date_input)
        print(f"You should reply with:\n\n {gptReponse}")
        print("\n")
if __name__ == "__main__":
    main()