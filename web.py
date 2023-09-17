from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
with open('key.txt', 'r') as file:
    openai.api_key = file.read().strip()

def get_reply(name, age, user_input, date_input):
    response = openai.Completion.create(
        engine = "davinci",
        prompt = f"{name}, a {age}-year-old individual, is on a date. Their date mentioned: '{date_input}'. In response, {name} said: '{user_input}'. Given this context, provide a clear and concise reply in elgish to what would be an appropriate and thoughtful reply for {name}'s date?",
        max_tokens = 50
    )
    return response.choices[0].text.strip()

    @app.route('/test')
    def test():
        return "Test route works!"

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/get-reply', methods = ['POST'])
    def reply():
        data = request.json
        name = data['name']
        age = data['age']
        user_input = data['user_input']
        date_input = data['date_input']

        gpt_response = get_reply(name, age, user_input, date_input)
    
        return jsonify({'reply': gpt_response})

if __name__ == '__main__':
    app.run(debug=True)