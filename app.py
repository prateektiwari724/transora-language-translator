import streamlit as st
from deep_translator import GoogleTranslator
import pyperclip

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="TRANSORA",
    layout="wide"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>

/* ================= MAIN APP ================= */
.stApp {
    background: linear-gradient(
        135deg,
        #fff1f2 0%,
        #ffe4e6 45%,
        #fef3c7 100%
    );
    color: #1e293b;
}

/* ================= REMOVE STREAMLIT ================= */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* ================= MAIN CONTAINER ================= */
.main-container {
    padding: 10px 3%;
}

/* ================= HERO ================= */
.hero {
    text-align: center;
    padding-top: 20px;
    padding-bottom: 10px;
}

.hero-title {
    font-size: 72px;
    font-weight: 900;
    letter-spacing: 2px;

    background: linear-gradient(
        to right,
        #ff6a00,
        #ff3d54,
        #ec4899
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 8px;
}

.hero-subtitle {
    color: #7c2d12;
    font-size: 24px;
    font-weight: 500;
    margin-bottom: 40px;
}

/* ================= INFO CARDS ================= */
.info-card {
    background: rgba(255,255,255,0.55);
    border-radius: 24px;
    padding: 18px 16px;
    text-align: center;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.6);
    box-shadow: 0 8px 22px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
    min-height: 140px;
}

.info-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 18px 35px rgba(0,0,0,0.08);
}

.info-number {
    font-size: 34px;
    font-weight: 800;
    color: #ea580c;
}

.info-label {
    margin-top: 6px;
    color: #7c2d12;
    font-size: 16px;
    font-weight: 500;
}

/* ================= SECTION TITLES ================= */
.section-title {
    font-size: 42px;
    font-weight: 800;
    color: #9a3412;
    margin-bottom: 20px;
    margin-top: 15px;
}

/* ================= TEXT AREAS ================= */
textarea {
    background: #ffffff !important;
    border-radius: 26px !important;
    border: 2px solid #fecaca !important;
    padding: 20px !important;

    height: 220px !important;
    min-height: 220px !important;
    max-height: 220px !important;

    font-size: 20px !important;

    color: #111827 !important;
    -webkit-text-fill-color: #111827 !important;
    caret-color: #111827 !important;

    opacity: 1 !important;

    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
}

/* INPUT TEXT COLOR */
textarea {
    color: #111827 !important;
}

/* TRANSLATED OUTPUT TEXT COLOR */
textarea[disabled] {
    color: #111827 !important;
    -webkit-text-fill-color: #111827 !important;
    opacity: 1 !important;
}

/* PLACEHOLDER */
textarea::placeholder {
    color: #6b7280 !important;
    opacity: 1 !important;
}

/* ================= LABELS ================= */
label {
    color: black !important;
    font-weight: 700 !important;
    font-size: 17px !important;
}

/* ================= DROPDOWNS ================= */
div[data-baseweb="select"] > div {
    background: #000000 !important;
    border-radius: 18px !important;
    border: 2px solid #000000 !important;
    min-height: 60px !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    color: white !important;
}

div[data-baseweb="select"] span {
    color: white !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}

div[data-baseweb="select"] input {
    color: white !important;
    -webkit-text-fill-color: white !important;
}

div[data-baseweb="select"] svg {
    fill: white !important;
}

/* ================= BUTTONS ================= */
.stButton > button,
.stDownloadButton > button {
    width: 100%;
    min-width: 220px;
    max-width: 220px;
    border: none;
    border-radius: 22px;
    height: 65px;
    font-size: 20px;
    font-weight: 700;
    color: white;

    background: linear-gradient(
        135deg,
        #ff6a00,
        #ff3d54,
        #ec4899
    );

    box-shadow: 0 10px 25px rgba(236,72,153,0.25);
    transition: all 0.3s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: 0 15px 35px rgba(236,72,153,0.35);
}

/* ================= SUCCESS BOX ================= */
.custom-msg {
    background-color: white;
    color: black;
    border: 2px solid black;
    padding: 16px;
    border-radius: 18px;
    font-size: 18px;
    font-weight: 700;
    margin-top: 10px;
}

/* ================= CHARACTER TEXT ================= */
.character-text {
    color: #374151;
    font-size: 17px;
    font-weight: 600;
    margin-top: 8px;
}

</style>
""", unsafe_allow_html=True)

# ================= LANGUAGES =================
languages = GoogleTranslator().get_supported_languages(as_dict=True)

formatted_languages = {
    lang.title(): code
    for lang, code in languages.items()
}

language_names = sorted(formatted_languages.keys())

# ================= SESSION STATE =================
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "source_lang" not in st.session_state:
    st.session_state.source_lang = "Auto Detect"

if "target_lang" not in st.session_state:
    st.session_state.target_lang = "Hindi"

# ================= MAIN CONTAINER =================
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# ================= HERO =================
st.markdown("""
<div class="hero">
    <div class="hero-title">TRANSORA</div>
    <div class="hero-subtitle">
        Smart AI-powered translation in 100+ languages
    </div>
</div>
""", unsafe_allow_html=True)

# ================= INFO CARDS =================
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="info-card">
        <div class="info-number">100+</div>
        <div class="info-label">Languages Supported</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="info-card">
        <div class="info-number">AI</div>
        <div class="info-label">Smart Translation Engine</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="info-card">
        <div class="info-number">FAST</div>
        <div class="info-label">Real-Time Translation</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ================= INPUT OUTPUT =================
left, right = st.columns(2)

with left:

    st.markdown(
        '<div class="section-title">Input Text</div>',
        unsafe_allow_html=True
    )

    input_text = st.text_area(
        "",
        value=st.session_state.input_text,
        height=320,
        placeholder="Type or paste your text here..."
    )

    st.session_state.input_text = input_text

with right:

    st.markdown(
        '<div class="section-title">Translated Text</div>',
        unsafe_allow_html=True
    )

    st.text_area(
        "",
        st.session_state.translated_text,
        height=320,
        disabled=True
    )

# ================= CHARACTER COUNT =================

# GET EXACT USER INPUT
raw_text = input_text if input_text else ""

# REMOVE ONLY STREAMLIT HIDDEN NEWLINES
# DO NOT REMOVE REAL USER SPACES
clean_text = raw_text.replace("\r", "")

# REMOVE ONLY ONE TRAILING NEWLINE
# ADDED INTERNALLY BY STREAMLIT text_area
if clean_text.endswith("\n"):
    clean_text = clean_text[:-1]

# EXACT CHARACTER COUNT
character_count = len(clean_text)

# SHOW CHARACTER COUNT
st.markdown(
    f'<div class="character-text">Characters: {character_count}</div>',
    unsafe_allow_html=True
)

# ================= LANGUAGE SECTION =================
st.write("")

source_options = ["Auto Detect"] + language_names

lang_left, lang_right = st.columns(2)

with lang_left:

    source_lang = st.selectbox(
        "Source Language",
        source_options,
        index=source_options.index(st.session_state.source_lang)
    )

with lang_right:

    target_lang = st.selectbox(
        "Target Language",
        language_names,
        index=language_names.index(st.session_state.target_lang)
    )

# SAVE LANGUAGES
st.session_state.source_lang = source_lang
st.session_state.target_lang = target_lang

# ================= BUTTONS =================
st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)

btn1, btn2, btn3, btn4, btn5 = st.columns(5)

with btn1:
    translate_clicked = st.button("Translate Now")

with btn2:
    clear_clicked = st.button("Clear")

with btn3:
    swap_clicked = st.button("Swap")

with btn4:

    if st.session_state.translated_text:

        if st.button("Copy Translation"):

            pyperclip.copy(
                st.session_state.translated_text
            )

            st.markdown(
                '<div class="custom-msg">Copied to clipboard!</div>',
                unsafe_allow_html=True
            )

with btn5:

    if st.session_state.translated_text:

        st.download_button(
            label="Download Translation",
            data=st.session_state.translated_text,
            file_name="translation.txt",
            mime="text/plain"
        )

# ================= SWAP =================
if swap_clicked:

    if st.session_state.source_lang != "Auto Detect":

        temp = st.session_state.source_lang

        st.session_state.source_lang = st.session_state.target_lang
        st.session_state.target_lang = temp

        st.rerun()

# ================= CLEAR =================
if clear_clicked:

    st.session_state.input_text = ""
    st.session_state.translated_text = ""
    st.session_state.source_lang = "Auto Detect"
    st.session_state.target_lang = "Hindi"

    st.rerun()

# ================= TRANSLATE =================
if translate_clicked:

    if input_text.strip() == "":

        st.markdown(
            '<div class="custom-msg">Please enter some text.</div>',
            unsafe_allow_html=True
        )

    elif (
        st.session_state.source_lang != "Auto Detect"
        and st.session_state.source_lang == st.session_state.target_lang
    ):

        st.markdown(
            '<div class="custom-msg">Source and target languages cannot be same.</div>',
            unsafe_allow_html=True
        )

    else:

        try:

            source_code = (
                "auto"
                if st.session_state.source_lang == "Auto Detect"
                else formatted_languages[
                    st.session_state.source_lang
                ]
            )

            target_code = formatted_languages[
                st.session_state.target_lang
            ]

            # ================= LOADING =================
            with st.spinner("Translating..."):

                translated = GoogleTranslator(
                    source=source_code,
                    target=target_code
                ).translate(input_text)

            # ================= SAVE OUTPUT =================
            st.session_state.translated_text = translated

            # ================= SUCCESS =================
            st.markdown(
                '<div class="custom-msg">Translation completed successfully!</div>',
                unsafe_allow_html=True
            )

            # REFRESH UI
            st.rerun()

        except Exception as e:

            st.markdown(
                f'<div class="custom-msg">Error: {e}</div>',
                unsafe_allow_html=True
            )