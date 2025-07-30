#!/bin/bash

echo "Setting up your chatbot environment..."

# Python requirements
echo "Installing Python and NLTK (if possible)..."
if command -v apt >/dev/null; then
    sudo apt update
    sudo apt install -y python3 python3-pip
    pip3 install --user nltk
elif command -v pkg >/dev/null; then
    pkg update
    pkg install -y python
    pip install --user nltk
fi

# Inform user about usage
echo
echo "Setup complete!"
echo "To run the Python version: python3 humanlike_chatbot.py"
echo "To run the Bash version: chmod +x bash_chatbot.sh && ./bash_chatbot.sh"
