import streamlit as st
from googletrans import Translator

st.set_page_config(page_title="Language Translation Tool", page_icon="🌍")

st.title("🌍 Language Translation Tool")
st.write("Translate text into different languages instantly.")

translator = Translator()

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko"
}

text = st.text_area("Enter Text")

source_lang = st.selectbox("Select Source Language", list(languages.keys()))
target_lang = st.selectbox("Select Target Language", list(languages.keys()))

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            translated = translator.translate(
                text,
                src=languages[source_lang],
                dest=languages[target_lang]
            )

            st.success("Translation Completed ✅")
            st.subheader("Translated Text:")
            st.write(translated.text)

        except Exception as e:
            st.error(f"Error: {e}")
