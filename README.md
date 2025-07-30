# Human-like Terminal Chatbot

A sophisticated chatbot designed to behave like a real human, with persistent memory and personality traits. Compatible with **Kali Linux** and **Termux**.

## ðŸŒŸ Features

- **Human-like Personality**: Configurable personality traits based on the Big Five model
- **Persistent Memory**: Stores conversations, user preferences, and personal data locally
- **Sentiment Analysis**: Understands and responds to user emotions
- **Cross-Platform**: Works on Kali Linux, Termux, and other Linux distributions
- **Dual Implementation**: Both Python and Bash versions available
- **Local Storage**: All data stored securely on your device
- **Conversation History**: Tracks and remembers past interactions
- **User Profiling**: Learns about users over time

## ðŸš€ Quick Start

### Automatic Setup
```bash
chmod +x setup.sh
./setup.sh
```

### Manual Installation

#### For Python Version:
```bash
# Install dependencies
pip install nltk

# Run the chatbot
python3 humanlike_chatbot.py
```

#### For Bash Version:
```bash
# Make executable
chmod +x bash_chatbot.sh

# Run the chatbot
./bash_chatbot.sh
```

## ðŸ’» Environment Compatibility

### Kali Linux
- Python 3.6+
- Bash 4.0+
- Standard Linux utilities

### Termux (Android)
- Install Termux from F-Droid (recommended) or Google Play
- Python and Bash packages
- Storage permission for data persistence

### Installation Commands:

**Kali Linux:**
```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install nltk
```

**Termux:**
```bash
pkg update
pkg install python git
pip install nltk
```

## ðŸ§  How It Works

### Python Implementation
- Uses NLTK for natural language processing
- JSON-based data storage
- Object-oriented design with modular components
- Advanced sentiment analysis
- Comprehensive memory management

### Bash Implementation
- Pure Bash scripting with no external dependencies
- File-based storage system
- Pattern matching for user input analysis
- Lightweight and fast
- Shell-native integration

## ðŸ“ Data Storage

The chatbot stores data in local files:

**Python Version:**
- `~/chatbot_data/memory.json` - Long-term memory
- `~/chatbot_data/personality.json` - Personality configuration
- `~/chatbot_data/conversations.json` - Conversation history
- `~/chatbot_data/user_profile.json` - User information

**Bash Version:**
- `~/.chatbot_data/memory.txt` - User facts and preferences
- `~/.chatbot_data/personality.txt` - Personality settings
- `~/.chatbot_data/conversations.txt` - Chat logs
- `~/.chatbot_data/user_profile.txt` - User profile data

## ðŸŽ­ Personality System

The chatbot's personality is based on:

- **Big Five Traits**: Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism
- **Speaking Style**: Formality level, emoji usage, humor, empathy
- **Interests**: Configurable topics of interest
- **Catchphrases**: Memorable expressions

## ðŸ’¬ Chat Commands

While chatting, you can use these special commands:

- `stats` - Show chatbot statistics
- `clear` - Clear all memory (use carefully!)
- `quit`, `exit`, `bye` - End the conversation

## ðŸ¤– Human-like Behaviors

### Conversation Memory
- Remembers your name, age, and interests
- References past conversations
- Builds relationship over time

### Emotional Intelligence
- Responds appropriately to positive/negative sentiment
- Shows empathy and understanding
- Adjusts responses based on your mood

### Personality Traits
- Consistent personality across conversations
- Curious and engaging responses
- Humor and wit when appropriate
- Supportive and encouraging

## ðŸ”§ Customization

### Modifying Personality (Python)
Edit `chatbot_data/personality.json`:
```json
{
  "traits": {
    "openness": 0.8,
    "conscientiousness": 0.7,
    "extraversion": 0.6,
    "agreeableness": 0.9,
    "neuroticism": 0.3
  }
}
```

### Modifying Personality (Bash)
Edit `~/.chatbot_data/personality.txt`:
```
friendliness=8
humor_level=6
curiosity=9
empathy=8
formality=3
```

## ðŸ› ï¸ Advanced Usage

### Running in Background
```bash
# Python version
nohup python3 humanlike_chatbot.py &

# Bash version
nohup ./bash_chatbot.sh &
```

### Integration with Other Scripts
```bash
# Source the bash functions
source bash_chatbot.sh

# Use individual functions
response=$(generate_response "Hello!" "positive")
echo "$response"
```

## ðŸ“Š Performance

- **Python Version**: More features, requires ~50MB RAM
- **Bash Version**: Lightweight, requires ~5MB RAM
- **Storage**: Minimal disk space usage (~1MB per 1000 conversations)
- **Speed**: Instant responses on modern hardware

## ðŸ”’ Privacy & Security

- **Local Storage**: All data stays on your device
- **No Network**: Works completely offline
- **Encrypted Storage**: Option for data encryption (advanced users)
- **User Control**: Complete control over data retention

## ðŸ› Troubleshooting

### Common Issues:

**Permission Denied:**
```bash
chmod +x humanlike_chatbot.py
chmod +x bash_chatbot.sh
```

**Module Not Found (Python):**
```bash
pip install nltk
python3 -c "import nltk; nltk.download('vader_lexicon')"
```

**Bash Script Errors:**
```bash
# Check bash version
bash --version  # Should be 4.0+
```

### Debug Mode:
```bash
# Python - enable verbose logging
python3 humanlike_chatbot.py --debug

# Bash - enable debug output
bash -x bash_chatbot.sh
```

## ðŸ¤ Contributing

Feel free to enhance the chatbot! Areas for improvement:
- Additional personality traits
- More sophisticated NLP
- Voice integration
- Multi-language support
- Advanced conversation patterns

## ðŸ“œ License

This project is open source. Use and modify as needed for your projects.

## ðŸ“ž Support

For issues or questions:
1. Check the troubleshooting section
2. Review the conversation logs for errors
3. Test with both Python and Bash versions

## ðŸ”® Future Features

- Voice input/output
- Web interface
- Multiple personality presets
- Conversation analytics
- Export/import conversations
- Cloud synchronization (optional)

---

**Enjoy chatting with your new AI companion!** ðŸ¤–ðŸ’¬
