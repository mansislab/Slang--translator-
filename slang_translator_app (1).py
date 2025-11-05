import streamlit as st

slang_dict = {
    "brb": "be right back",
    "lol": "laughing out loud",
    "idk": "I don't know",
    "btw": "by the way",
    "omg": "oh my god",
    "tbh": "to be honest",
    "smh": "shaking my head",
    "afaik": "as far as I know",
    "irl": "in real life",
    "lit": "amazing",
    "sus": "suspicious",
    "cap": "lie",
    "no cap": "no lie",
    "salty": "bitter or upset",
    "fam": "close friend or family",
    "flex": "show off",
    "vibe": "atmosphere or feeling"
}

formal_to_slang = {v: k for k, v in slang_dict.items()}

def translate_slang_to_normal(text):
    words = text.lower().split()
    return " ".join([slang_dict.get(w, w) for w in words])

def translate_normal_to_slang(text):
    words = text.lower().split()
    return " ".join([formal_to_slang.get(w, w) for w in words])

st.set_page_config(page_title="Slang Translator 😎", page_icon="🗣️", layout="centered")
st.title("🗣️ Slang Translator")
st.write("Translate between slang and normal English — powered by Python 💻")

mode = st.radio("Choose translation direction:", ["Slang ➡ Normal English", "Normal English ➡ Slang"])
text = st.text_area("Enter your sentence:", placeholder="Type something like 'brb lol that was lit fam'")

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter a sentence first!")
    else:
        if mode == "Slang ➡ Normal English":
            result = translate_slang_to_normal(text)
        else:
            result = translate_normal_to_slang(text)
        st.success(f"**Translation:** {result}")
