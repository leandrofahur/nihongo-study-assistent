import streamlit as st
import pandas as pd
import genanki
import platform
import tempfile
import os

# Set page config
st.set_page_config(
    page_title="Nihongo Study Assistant - Quizlet to Anki Converter",
    page_icon="🎌",
    layout="wide"
)

# Custom CSS to improve the look
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    .stTextArea>div>div>textarea {
        font-family: monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# Define Anki model for Japanese cards
model = genanki.Model(
    1607392319,
    'Japanese Vocabulary Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Japanese → English',
            'qfmt': '<div style="font-size: 24px; text-align: center;">{{Question}}</div>',
            'afmt': '''
                <div style="font-size: 24px; text-align: center;">{{Question}}</div>
                <hr>
                <div style="font-size: 20px; text-align: center;">{{Answer}}</div>
            ''',
        },
    ],
    css='''
        .card {
            font-family: "Hiragino Kaku Gothic Pro", "Arial", sans-serif;
            text-align: center;
            color: black;
            background-color: white;
        }
    '''
)

# Define Anki deck
deck = genanki.Deck(
    2059400110,
    'Japanese Vocabulary (Import)'
)

def create_notes_from_text(text_content):
    """Create Anki notes from text content."""
    # Clear existing notes (in case of multiple submissions)
    deck.notes = []
    
    # Split text into lines and process each line
    lines = [line.strip() for line in text_content.split('\n') if line.strip()]
    
    for line in lines:
        # Skip empty lines or lines without a separator
        if not line or ' - ' not in line:
            continue
            
        # Split line into front and back parts
        front, back = line.split(' - ', 1)
        
        note = genanki.Note(
            model=model,
            fields=[front.strip(), back.strip()]
        )
        deck.add_note(note)
    
    return len(deck.notes)

# Main app layout
st.title('🎌 Nihongo Study Assistant')
st.subheader('Quizlet to Anki Converter')

# OS detection and installation instructions
os_type = platform.system()
with st.expander("📥 Anki Installation Instructions", expanded=True):
    if os_type == 'Darwin':  # macOS
        st.markdown("""
            ### macOS Installation Steps:
            1. Visit the [Anki download page](https://apps.ankiweb.net/)
            2. Click on the macOS download button
            3. Open the downloaded .dmg file
            4. Drag Anki to your Applications folder
            5. Open Anki from your Applications folder
            """)
    elif os_type == 'Windows':
        st.markdown("""
            ### Windows Installation Steps:
            1. Visit the [Anki download page](https://apps.ankiweb.net/)
            2. Click on the Windows download button
            3. Run the downloaded installer
            4. Follow the installation wizard
            5. Launch Anki from the Start menu
            """)
    elif os_type == 'Linux':
        st.markdown("""
            ### Linux Installation Steps:
            1. Open your terminal
            2. Run: `sudo apt install anki` (Ubuntu/Debian)
            3. Or visit [Anki download page](https://apps.ankiweb.net/) for other distributions
            4. Launch Anki from your applications menu
            """)
    else:
        st.warning("Your operating system is not recognized. Please visit [Anki's website](https://apps.ankiweb.net/) for installation instructions.")

# Text input section
st.markdown("### 📝 Enter Your Vocabulary")
st.markdown("""
    Enter your vocabulary pairs, one per line, using the format:
    ```
    Japanese - English
    ```
    For example:
    ```
    日本語 - Japanese
    こんにちは - Hello
    ありがとう - Thank you
    ```
""")

text_input = st.text_area(
    "Enter your vocabulary pairs here:",
    height=300,
    placeholder="日本語 - Japanese\nこんにちは - Hello\nありがとう - Thank you"
)

if st.button("Convert to Anki Deck"):
    if not text_input.strip():
        st.error("❌ Please enter some vocabulary pairs!")
    else:
        try:
            num_cards = create_notes_from_text(text_input)
            if num_cards == 0:
                st.error("❌ No valid vocabulary pairs found. Please check the format!")
            else:
                st.success(f'✅ Successfully processed {num_cards} cards!')
                
                # Generate and offer download of .apkg file
                with st.spinner('Generating Anki deck...'):
                    package = genanki.Package(deck)
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.apkg') as tmp:
                        package.write_to_file(tmp.name)
                        with open(tmp.name, 'rb') as f:
                            st.download_button(
                                label="⬇️ Download Anki Deck",
                                data=f,
                                file_name='Japanese_Vocabulary.apkg',
                                mime='application/octet-stream'
                            )
                
                st.markdown("""
                    ### Next Steps:
                    1. Download the Anki deck using the button above
                    2. Double-click the downloaded file to import it into Anki
                    3. Start studying! 🎉
                """)
                
        except Exception as e:
            st.error(f'❌ An unexpected error occurred: {str(e)}')

# Footer
st.markdown("---")
st.markdown("Made with ❤️ for Japanese learners") 