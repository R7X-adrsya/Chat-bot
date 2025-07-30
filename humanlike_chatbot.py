import os
import json
import datetime
try:
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    import nltk
except ImportError:
    SentimentIntensityAnalyzer = None

DATA_DIR = os.path.expanduser('~/chatbot_data/')
USER_FILE = os.path.join(DATA_DIR, 'user.json')
HISTORY_FILE = os.path.join(DATA_DIR, 'history.json')
PERSONALITY_FILE = os.path.join(DATA_DIR, 'personality.json')

def ensure_dirs():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_json(filename, default):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return default

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def sentiment(text):
    if SentimentIntensityAnalyzer:
        sid = SentimentIntensityAnalyzer()
        scores = sid.polarity_scores(text)
        if scores['compound'] >= 0.05:
            return "positive"
        elif scores['compound'] <= -0.05:
            return "negative"
        else:
            return "neutral"
    # Fallback
    pos = ("great", "good", "awesome", "love", "wonderful", "nice", "happy")
    neg = ("hate", "bad", "terrible", "sad", "angry", "upset", "dislike")
    for word in pos:
        if word in text:
            return "positive"
    for word in neg:
        if word in text:
            return "negative"
    return "neutral"

def detect_name(user, text):
    import re
    m = re.search(r"\bmy name is (\w+)", text, re.IGNORECASE)
    if m:
        user['name'] = m.group(1)
    return user

def respond(text, user, persona, context):
    s = sentiment(text)
    user = detect_name(user, text)
    response = ""
    if 'name' not in user:
        response = "Hey! What's your name?"
    elif text.lower() in ('bye', 'exit', 'quit'):
        response = f"Bye {user['name']}! It was a pleasure chatting with you."
    elif text.lower() == 'stats':
        response = f"Your name: {user.get('name','Unknown')}\nChats: {len(context)}"
    elif text.lower() == "clear":
        context.clear()
        user.clear()
        response = "Memory erased. Let's start fresh!"
    elif s == "negative":
        response = f"I'm sorry to hear that, {user['name']}. Do you want to talk about it?"
    elif s == "positive":
        response = f"That's awesome, {user['name']}! Tell me more."
    else:
        response = persona.get('casual', "Let's chat! What would you like to talk about?")
    # Memory: save preferences, basic facts
    if "I like" in text:
        user.setdefault('likes', []).append(text.split("I like")[-1].strip())
        response += f" Noted that you like {user['likes'][-1]}!"
    return response, user

def main():
    ensure_dirs()
    user = load_json(USER_FILE, {})
    persona = load_json(PERSONALITY_FILE, {
        "traits": {
            "agreeableness": 0.8,
            "conscientiousness": 0.7,
            "extraversion": 0.6
        },
        "casual": "I'm all ears. What's on your mind?"
    })
    history = load_json(HISTORY_FILE, [])
    print("ChatBot: Hi! (type 'bye' to exit)")
    while True:
        inp = input(f"{user.get('name','You')}: ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        chat_entry = {"user": inp, "time": timestamp}
        reply, user = respond(inp, user, persona, history)
        history.append({"user": inp, "bot": reply, "sentiment": sentiment(inp), "time": timestamp})
        print("ChatBot:", reply)
        save_json(HISTORY_FILE, history)
        save_json(USER_FILE, user)
        if inp.lower() in ('bye', 'exit', 'quit'):
            break

if __name__ == "__main__":
    main()
