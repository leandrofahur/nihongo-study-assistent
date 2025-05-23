import os
import json

import streamlit as st


# Load sentence data
with open("app/sentences.json", "r", encoding="utf-8") as f:
    sentences = json.load(f)

# App UI
st.title("🎙️ Japanese Speaking Practice")
st.markdown(f"1. Select a sentence to practice:")

# Sentence selector
sentence_options = [f"{s['japanese']} ({s['translation']})" for s in sentences]
choice = st.selectbox("Choose a sentence to practice:", sentence_options)


# Get selected sentence
selected = sentences[sentence_options.index(choice)]
st.markdown(f"**Selected Sentence:** {selected['japanese']}")
st.markdown(f"**Romaji**: {selected['romaji']}")
st.markdown(f"**Translation**: {selected['translation']}")

# Audio recorder
audio_value = st.audio_input("2. Record your pronunciation")

if audio_value:    
    st.audio(audio_value)

# # Audio playback
# audio_path = f"audio/{selected['id']}_{selected['romaji'].replace(' ', '_')}.mp3"
# if os.path.exists(audio_path):
#     with open(audio_path, 'rb') as audio_file:
#         st.audio(audio_file.read(), format='audio/mp3')
# else:
#     st.warning("Audio not found.")

# # Record user's voice
# st.subheader("🎤 Record your pronunciation")
# audio_bytes = audio_recorder(pause_threshold=2.0)

# if audio_bytes:
#     # Save the recording
#     file_name = f"recordings/{selected['id']}_recording.wav"
#     with open(file_name, "wb") as f:
#         f.write(audio_bytes)
#     st.success("Recording saved!")
#     st.audio(audio_bytes, format='audio/wav')
