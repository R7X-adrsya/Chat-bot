#!/usr/bin/env python3
"""
Enhanced Human-like Chatbot with Improved Response Logic
Auto default fallback (no manual typing required)
"""

import os
import json
import datetime
import re
import random

try:
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    import nltk
    NLTK_AVAILABLE = True
except ImportError:
    SentimentIntensityAnalyzer = None
    NLTK_AVAILABLE = False

DATA_DIR = os.path.expanduser('~/chatbot_data/')
USER_FILE = os.path.join(DATA_DIR, 'user.json')
HISTORY_FILE = os.path.join(DATA_DIR, 'history.json')
PERSONALITY_FILE = os.path.join(DATA_DIR, 'personality.json')


def ensure_dirs():
    """Create necessary directories if they don't exist"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def load_json(filename, default):
    """Load JSON file with error handling"""
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return default
    return default


def save_json(filename, data):
    """Save JSON file with error handling"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[Warning] Could not save {filename}: {e}")


def enhanced_sentiment_analysis(text):
    """Improved sentiment analysis with fallback"""
    text_lower = text.lower().strip()

    # Try VADER first
    if NLTK_AVAILABLE and SentimentIntensityAnalyzer:
        try:
            analyzer = SentimentIntensityAnalyzer()
            scores = analyzer.polarity_scores(text)
            compound = scores['compound']
            if compound >= 0.1:
                return "positive"
            elif compound <= -0.1:
                return "negative"
            else:
                return "neutral"
        except:
            pass  # fallback

    # Keyword fallback
    positive_keywords = ["love", "amazing", "awesome", "fantastic", "wonderful",
                         "excellent", "great", "good", "happy", "excited"]
    negative_keywords = ["hate", "terrible", "awful", "horrible",
                         "worst", "bad", "sad", "angry", "upset", "frustrated"]

    if any(word in text_lower for word in positive_keywords):
        return "positive"
    elif any(word in text_lower for word in negative_keywords):
        return "negative"
    return "neutral"


def extract_user_info(text, user):
    """Extract and store user details"""
    text_lower = text.lower()
    updated = False

    # Name
    name_patterns = [
        r"my name is (\w+)",
        r"i am (\w+)",
        r"i'm (\w+)",
        r"call me (\w+)"
    ]
    for pattern in name_patterns:
        match = re.search(pattern, text_lower)
        if match:
            name = match.group(1).capitalize()
            user['name'] = name
            updated = True
            break

    # Age
    age_match = re.search(r"(\d+)\s*(years old|year old)?", text_lower)
    if age_match:
        user['age'] = int(age_match.group(1))
        updated = True

    # Interests
    interest_patterns = [
        r"i like (.+)",
        r"i love (.+)",
        r"i enjoy (.+)"
    ]
    for pattern in interest_patterns:
        match = re.search(pattern, text_lower)
        if match:
            interest = match.group(1).strip()
            if len(interest) < 50:
                user.setdefault('interests', []).append(interest)
                updated = True
    return user, updated


def get_contextual_response(text, user, sentiment, history_length):
    """Generate chatbot responses"""
    text_lower = text.lower().strip()
    user_name = user.get('name', 'friend')

    # Commands
    if text_lower in ['bye', 'goodbye', 'exit', 'quit']:
        return f"Goodbye {user_name}! Take care 👋"

    if text_lower == 'stats':
        stats = (f"📊 Stats:\n"
                 f"Name: {user.get('name', 'Unknown')}\n"
                 f"Age: {user.get('age', 'Not given')}\n"
                 f"Messages: {history_length}\n"
                 f"Interests: {', '.join(user.get('interests', [])) or 'None'}")
        return stats

    if text_lower in ['clear', 'reset']:
        return "🔄 Memory cleared! Let's start fresh. What's your name?"

    if text_lower in ['help', 'commands']:
        return "💡 Commands: stats, clear, help, bye\nOtherwise, just chat with me!"

    # Greetings
    if re.search(r"\b(hi|hello|hey)\b", text_lower):
        if 'name' in user:
            return f"Hello {user_name}! How are you doing today?"
        else:
            return "Hello! 😊 What's your name?"

    # About bot
    if "who are you" in text_lower or "your name" in text_lower:
        return f"I'm your friendly chatbot, {user_name}! I love conversations."

    # How are you
    if "how are you" in text_lower:
        return f"I'm doing great, {user_name}! How about you?"

    # Sentiment
    if sentiment == "positive":
        return f"That's wonderful, {user_name}! 😄"
    elif sentiment == "negative":
        return f"I'm sorry to hear that, {user_name}. 😔"

    # Default fallback response (auto-generated)
    default_responses = [
        f"That's interesting, {user_name}. Can you tell me more?",
        f"I see, {user_name}. What do you think about that?",
        f"Thanks for sharing, {user_name}. How does that make you feel?",
        f"Hmm, that sounds important, {user_name}. Could you explain more?",
        f"I'm curious, {user_name}. Tell me more!"
    ]
    return random.choice(default_responses)


def process_user_input(text, user, history):
    """Main input processor"""
    text = text.strip()
    if not text:
        return "I didn't catch that. Could you say something?", user

    user, _ = extract_user_info(text, user)
    sentiment = enhanced_sentiment_analysis(text)
    response = get_contextual_response(text, user, sentiment, len(history))
    return response, user


def main():
    """Main chatbot loop"""
    print("🤖 Enhanced Chatbot Started")
    print("Type 'help' for commands, 'bye' to exit\n")

    ensure_dirs()
    user = load_json(USER_FILE, {})
    history = load_json(HISTORY_FILE, [])

    if user.get('name'):
        print(f"ChatBot: Welcome back, {user['name']}! 😊")
    else:
        print("ChatBot: Hello! What's your name?")

    while True:
        try:
            user_input = input(f"{user.get('name', 'You')}: ")
            response, user = process_user_input(user_input, user, history)

            print(f"ChatBot: {response}")

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history.append({
                "user": user_input,
                "bot": response,
                "sentiment": enhanced_sentiment_analysis(user_input),
                "time": timestamp
            })

            save_json(USER_FILE, user)
            save_json(HISTORY_FILE, history)

            if user_input.lower() in ['bye', 'exit', 'quit']:
                break

        except KeyboardInterrupt:
            print("\nChatBot: Goodbye! 👋")
            break


if __name__ == "__main__":
    main()
    
