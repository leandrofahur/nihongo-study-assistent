# Nihongo Study Assistant 🎌

A Streamlit web application that helps Japanese language learners convert their vocabulary lists to Anki decks. This tool makes it easy to create Anki flashcards for studying Japanese.

## Features

- 🔤 Simple text-based vocabulary input
- 📱 OS-specific Anki installation instructions
- 🎨 Beautiful, user-friendly interface
- 💾 Easy one-click deck download
- 🔍 Input format validation
- 🎌 Optimized for Japanese language learning

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/nihongo-study-assistant.git
   cd nihongo-study-assistant
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to the displayed URL (usually http://localhost:8501)

3. Follow the on-screen instructions to:
   - Install Anki (if not already installed)
   - Enter your vocabulary pairs
   - Download and import the generated Anki deck

## Input Format

Enter your vocabulary pairs using this format:
```
Japanese - English
```

For example:
```
日本語 - Japanese
こんにちは - Hello
ありがとう - Thank you
```

Each line should contain exactly one vocabulary pair, with the Japanese term and its English translation separated by ` - ` (hyphen with spaces).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.