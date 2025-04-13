import spacy
import datetime


nlp = spacy.load("en_core_web_sm")

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


user_name = None


def clean_message_spacy(message):
    doc = nlp(message.lower())
    return [token.text for token in doc if not token.is_stop and not token.is_punct]


def solve_math_problem(problem):
    try:
        allowed_operators = ['+', '-', '*', '/']
        if any(op in problem for op in allowed_operators):
result = eval(problem)
            return f"The answer is: {result}"
        else:
            return "Sorry, I couldn't understand that math problem."
    except Exception:
return "Sorry, I couldn't do that. Try again."


def generate_bot_response(message):
    global user_name

    words = clean_message_spacy(message)

    
    if "hello" in words or "hi" in words or "hey" in words:
        if user_name:
return f"Hello, {user_name}! How can I assist you today?"
        else:
            return "Hello! What’s your name?"


elif "my name is" in message.lower() or "i am" in message.lower():
        name = message.split()[-1]
        user_name = name
        return f"Nice to meet you, {user_name}! How can I help you today?"

elif "how" in words and "you" in words:
return "I'm a bot, but I'm doing great! How about you?"

    elif "bye" in words or "goodbye" in words:
        return "Goodbye! Have a great day ????"
    

if any(op in message for op in ['+', '-', '*', '/']):
        return solve_math_problem(message)

  
    if "who" in words or "what" in words:
        return get_gk_answer(message)

    if "joke" in words:
return "Why don't skeletons fight with each other? They don't have the guts!"

    if "weather" in words:
        return "I can't retrieve the weather for you, but I suggest looking at your local weather service!"

if "remind" in text:
        return "Okay, what do you want me to remind you of?"

    return "Sorry, I didn't get that. Ask me something else!"

def get_gk_answer(question):
    gk_responses = {
"who is the president of the united states?": "Joe Biden is the President of the United States.",
        "what is the capital of france?": "Paris is the capital of France.",
    }
    return gk_responses.get(question.lower(), "I don't know the answer to that question.")

def get_current_time_and_date():
    now = datetime.datetime.now()
    return now.strftime("Current date and time: %Y-%m-%d %H:%M:%S")

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    response = generate_bot_response(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
