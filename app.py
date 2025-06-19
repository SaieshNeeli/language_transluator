import streamlit as st
from googletrans import Translator, LANGUAGES

# Translator instance
translator = Translator()

st.title("🌐 Auto Language Translator")
st.markdown("Enter your text, and it will be translated to your selected language.")

# Select target language
language_names = list(LANGUAGES.values())
language_codes = list(LANGUAGES.keys())
lang_name_to_code = {v: k for k, v in LANGUAGES.items()}

target_lang = st.selectbox("Select Target Language", language_names, index=language_names.index("hindi"))

# Input text
text = st.text_area("Enter text (in any language):")

# Translate
if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        try:
            # Translate (auto-detect source)
            dest_code = lang_name_to_code[target_lang]
            translated = translator.translate(text, dest=dest_code)

            # Show detected language
            detected_lang_name = LANGUAGES.get(translated.src, "Unknown")
            st.markdown(f"**Detected Language:** `{detected_lang_name}`")
            
            # Show translation
            st.markdown("### Translated Text")
            st.success(translated.text)
        except Exception as e:
            st.error(f"Translation failed: {str(e)}")
