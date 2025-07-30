#!/bin/bash

DATA_DIR="$HOME/.chatbot_data"
USER_FILE="$DATA_DIR/user.txt"
HISTORY_FILE="$DATA_DIR/history.txt"
mkdir -p "$DATA_DIR"

get_name() {
    if ! grep -q '^name=' "$USER_FILE" 2>/dev/null; then
        echo "ChatBot: What's your name?"
        read name
        echo "name=$name" >> "$USER_FILE"
    else
        name=$(grep '^name=' "$USER_FILE" | head -n1 | cut -d= -f2)
    fi
}

save_fact() {
    echo "$1" >> "$USER_FILE"
}

get_name

echo "ChatBot: Hi $name! Type 'bye' to exit."
while true; do
    printf "$name: "
    read msg
    echo "$name: $msg" >> "$HISTORY_FILE"
    if [[ "$msg" =~ bye|exit|quit ]]; then
        echo "ChatBot: Goodbye $name!"
        break
    elif [[ "$msg" == "clear" ]]; then
        > "$USER_FILE"
        > "$HISTORY_FILE"
        echo "ChatBot: Memory cleared."
        get_name
    elif [[ "$msg" == "stats" ]]; then
        chats=$(wc -l < "$HISTORY_FILE")
        echo "ChatBot: You've sent $chats messages."
    elif [[ "$msg" =~ "I like" ]]; then
        like=$(echo "$msg" | sed -n 's/.*I like //p')
        save_fact "like=$like"
        echo "ChatBot: Noted that you like $like."
    elif [[ "$msg" == *"sad"* || "$msg" == *"angry"* || "$msg" == *"upset"* ]]; then
        echo "ChatBot: Sorry to hear that, $name. Want to talk about it?"
    elif [[ "$msg" == *"happy"* || "$msg" == *"great"* ]]; then
        echo "ChatBot: That's awesome, $name!"
    else
        echo "ChatBot: Let's chat! What's on your mind?"
    fi
done
