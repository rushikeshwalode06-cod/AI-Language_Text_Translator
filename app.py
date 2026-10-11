import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# PREMIUM DESIGN
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
);

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(124,58,237,0.22),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(236,72,153,0.18),
            transparent 28%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(59,130,246,0.10),
            transparent 30%
        ),
        #070711;

    color: white;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* =========================================================
   SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #0b0a18,
            #10091c,
            #090812
        );

    border-right:
        1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label {
    color: white !important;
}


/* =========================================================
   HERO
========================================================= */

.hero-title {
    font-size: 48px;
    font-weight: 800;
    line-height: 1.1;

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #ddd6fe,
            #f9a8d4
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-top: 12px;
}

.hero-text {
    color: #cbd5e1;

    font-size: 17px;

    line-height: 1.7;

    max-width: 900px;

    margin-top: 12px;
}


/* =========================================================
   SECTION TITLES
========================================================= */

.section-title {
    font-size: 25px;
    font-weight: 800;

    color: white;

    margin-top: 28px;
    margin-bottom: 8px;
}

.section-subtitle {
    color: #94a3b8;

    font-size: 14px;

    margin-bottom: 15px;
}


/* =========================================================
   SELECT BOX
========================================================= */

div[data-baseweb="select"] > div {

    background:
        rgba(17,16,31,0.95) !important;

    border:
        1px solid rgba(139,92,246,0.35) !important;

    border-radius: 14px !important;

    color: white !important;
}


/* =========================================================
   TEXT AREA
========================================================= */

textarea {

    background:
        linear-gradient(
            145deg,
            rgba(17,16,31,0.98),
            rgba(12,11,24,0.98)
        ) !important;

    color: #f8fafc !important;

    border:
        1px solid rgba(139,92,246,0.30) !important;

    border-radius: 18px !important;

    padding: 18px !important;

    font-size: 15px !important;

    line-height: 1.7 !important;
}

textarea:focus {

    border:
        1px solid rgba(168,85,247,0.75) !important;

    box-shadow:
        0 0 0 2px rgba(168,85,247,0.10),
        0 15px 40px rgba(0,0,0,0.25) !important;
}


/* =========================================================
   BUTTONS
========================================================= */

.stButton > button {

    min-height: 52px;

    border-radius: 15px;

    border:
        1px solid rgba(255,255,255,0.15);

    background:
        linear-gradient(
            135deg,
            #7c3aed,
            #9333ea,
            #db2777
        );

    color: white;

    font-size: 15px;

    font-weight: 800;

    box-shadow:
        0 12px 30px rgba(124,58,237,0.30);

    transition: 0.25s;
}

.stButton > button:hover {

    transform: translateY(-3px);

    box-shadow:
        0 18px 40px rgba(168,85,247,0.40);
}


/* =========================================================
   DOWNLOAD BUTTON
========================================================= */

.stDownloadButton > button {

    min-height: 52px;

    border-radius: 15px;

    border: none;

    background:
        linear-gradient(
            135deg,
            #ec4899,
            #8b5cf6
        );

    color: white;

    font-weight: 800;

    transition: 0.25s;
}

.stDownloadButton > button:hover {

    transform: translateY(-3px);
}


/* =========================================================
   METRICS
========================================================= */

div[data-testid="stMetric"] {

    min-height: 130px;

    padding: 20px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(23,21,42,0.96),
            rgba(13,12,26,0.96)
        );

    border:
        1px solid rgba(139,92,246,0.25);

    box-shadow:
        0 15px 40px rgba(0,0,0,0.28);

    transition: 0.25s;
}

div[data-testid="stMetric"]:hover {

    transform: translateY(-4px);

    border-color:
        rgba(168,85,247,0.55);
}

div[data-testid="stMetricLabel"] {

    color: #a78bfa !important;

    font-weight: 700 !important;
}

div[data-testid="stMetricValue"] {

    color: white !important;

    font-size: 27px !important;

    font-weight: 800 !important;
}


/* =========================================================
   CARDS
========================================================= */

div[data-testid="stVerticalBlockBorderWrapper"] {

    background:
        linear-gradient(
            145deg,
            rgba(23,21,42,0.94),
            rgba(12,11,25,0.94)
        );

    border-color:
        rgba(139,92,246,0.28) !important;

    border-radius: 20px !important;

    box-shadow:
        0 12px 35px rgba(0,0,0,0.25);

    transition: 0.25s;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {

    border-color:
        rgba(168,85,247,0.60) !important;

    transform: translateY(-3px);
}


/* =========================================================
   CODE BOX
========================================================= */

div[data-testid="stCode"] {

    border-radius: 18px !important;

    border:
        1px solid rgba(139,92,246,0.30) !important;

    box-shadow:
        0 15px 40px rgba(0,0,0,0.25) !important;
}


/* =========================================================
   DIVIDER
========================================================= */

.gradient-divider {

    height: 1px;

    margin: 35px 0;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(168,85,247,0.55),
            rgba(236,72,153,0.55),
            transparent
        );
}


/* =========================================================
   FOOTER
========================================================= */

.footer {

    text-align: center;

    color: #64748b;

    font-size: 13px;

    margin-top: 45px;

    padding-top: 25px;

    border-top:
        1px solid rgba(255,255,255,0.06);
}


@media (max-width: 768px) {

    .hero-title {
        font-size: 34px;
    }

    .hero-text {
        font-size: 14px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# MODEL
# =========================================================

MODEL_NAME = "facebook/nllb-200-distilled-600M"


# =========================================================
# LANGUAGES
# =========================================================

LANGUAGES = {

    "English": "eng_Latn",
    "Hindi": "hin_Deva",
    "French": "fra_Latn",
    "German": "deu_Latn",
    "Spanish": "spa_Latn",
    "Italian": "ita_Latn",
    "Portuguese": "por_Latn",
    "Russian": "rus_Cyrl",
    "Chinese (Simplified)": "zho_Hans",
    "Japanese": "jpn_Jpan",
    "Korean": "kor_Hang",
    "Arabic": "arb_Arab",
    "Bengali": "ben_Beng",
    "Marathi": "mar_Deva",
    "Gujarati": "guj_Gujr",
    "Punjabi": "pan_Guru",
    "Tamil": "tam_Taml",
    "Telugu": "tel_Telu",
    "Kannada": "kan_Knda",
    "Malayalam": "mal_Mlym",
    "Urdu": "urd_Arab",
    "Nepali": "npi_Deva",
    "Dutch": "nld_Latn",
    "Turkish": "tur_Latn",
    "Vietnamese": "vie_Latn",
    "Thai": "tha_Thai",
    "Polish": "pol_Latn",
    "Ukrainian": "ukr_Cyrl",
    "Greek": "ell_Grek",
    "Romanian": "ron_Latn",
    "Swedish": "swe_Latn",
    "Danish": "dan_Latn",
    "Finnish": "fin_Latn",
    "Czech": "ces_Latn",
    "Hungarian": "hun_Latn",
    "Hebrew": "heb_Hebr",
    "Persian": "pes_Arab",
    "Swahili": "swh_Latn",
    "Indonesian": "ind_Latn",
    "Malay": "zsm_Latn",
    "Filipino": "tgl_Latn"
}


# =========================================================
# INITIAL SESSION STATE
# =========================================================

if "source_language" not in st.session_state:
    st.session_state.source_language = "English"

if "target_language" not in st.session_state:
    st.session_state.target_language = "Hindi"

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

if "translation_done" not in st.session_state:
    st.session_state.translation_done = False


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        MODEL_NAME
    )

    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )

    model.to(device)

    model.eval()

    return tokenizer, model, device


with st.spinner(
    "🌍 Loading multilingual AI model..."
):

    tokenizer, model, device = load_model()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🌍 AI Translator")

    st.caption(
        "Multilingual Translation Dashboard"
    )

    st.divider()

    st.markdown("### 🤖 Model")

    st.info(
        "NLLB-200"
    )

    st.markdown("### ⚡ Device")

    if torch.cuda.is_available():

        st.success(
            "🚀 GPU Enabled"
        )

    else:

        st.warning(
            "💻 CPU Mode"
        )

    st.divider()

    st.markdown("### 📌 Features")

    st.write("🌍 Multilingual Translation")
    st.write("🔄 Language Swap")
    st.write("📋 Copy Translation")
    st.write("⬇️ Download Translation")
    st.write("📊 Translation Statistics")
    st.write("⚡ GPU / CPU Support")

    st.divider()

    st.caption(
        "Powered by Hugging Face Transformers"
    )


# =========================================================
# HERO SECTION
# =========================================================

with st.container(border=True):

    st.markdown(
        "🌍 AI POWERED • MULTILINGUAL TRANSLATION"
    )

    st.markdown(
        '<div class="hero-title">'
        'Break Language Barriers With AI'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-text">'
        'Translate text between multiple languages '
        'using a powerful multilingual Transformer model.'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# LANGUAGE SELECTION
# =========================================================

st.markdown(
    '<div class="section-title">'
    '🌐 Choose Languages'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Select your source and target languages.'
    '</div>',
    unsafe_allow_html=True
)


source_col, swap_col, target_col = st.columns(
    [5, 1, 5]
)


# =========================================================
# SOURCE LANGUAGE
# =========================================================

with source_col:

    source_language = st.selectbox(
        "From",
        list(LANGUAGES.keys()),
        index=list(
            LANGUAGES.keys()
        ).index(
            st.session_state.source_language
        ),
        key="source_select"
    )


# =========================================================
# SWAP
# =========================================================

with swap_col:

    st.write("")
    st.write("")

    if st.button(
        "🔄",
        use_container_width=True
    ):

        current_source = st.session_state.source_language

        current_target = st.session_state.target_language

        st.session_state.source_language = current_target

        st.session_state.target_language = current_source

        st.rerun()


# =========================================================
# TARGET LANGUAGE
# =========================================================

with target_col:

    target_language = st.selectbox(
        "To",
        list(LANGUAGES.keys()),
        index=list(
            LANGUAGES.keys()
        ).index(
            st.session_state.target_language
        ),
        key="target_select"
    )


# =========================================================
# UPDATE SESSION LANGUAGE
# =========================================================

st.session_state.source_language = source_language
st.session_state.target_language = target_language


# =========================================================
# INPUT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">'
    '📝 Enter Your Text'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Type or paste the text you want to translate.'
    '</div>',
    unsafe_allow_html=True
)


# IMPORTANT:
# Input is stored in session_state so it remains visible
# after Streamlit reruns.

input_text = st.text_area(
    "Source Text",
    value=st.session_state.input_text,
    height=220,
    placeholder="Type or paste your text here...",
    key="input_box",
    label_visibility="collapsed"
)

st.session_state.input_text = input_text


# =========================================================
# TRANSLATION FUNCTION
# =========================================================

def translate_text(
    text,
    source_code,
    target_code
):

    tokenizer.src_lang = source_code

    encoded = tokenizer(
        text,
        return_tensors="pt",
        max_length=512,
        truncation=True
    )

    encoded = {
        key: value.to(device)
        for key, value in encoded.items()
    }

    target_token_id = tokenizer.convert_tokens_to_ids(
        target_code
    )

    with torch.no_grad():

        generated_tokens = model.generate(
            **encoded,
            forced_bos_token_id=target_token_id,
            max_new_tokens=512,
            num_beams=4,
            early_stopping=True
        )

    translated = tokenizer.batch_decode(
        generated_tokens,
        skip_special_tokens=True
    )[0]

    return translated


# =========================================================
# TRANSLATE BUTTON
# =========================================================

st.write("")

left, center, right = st.columns(
    [1, 2, 1]
)

with center:

    translate_clicked = st.button(
        "🌍  TRANSLATE NOW",
        use_container_width=True
    )


# =========================================================
# TRANSLATION PROCESS
# =========================================================

if translate_clicked:

    if not input_text.strip():

        st.warning(
            "⚠️ Please enter some text first."
        )

    elif source_language == target_language:

        st.warning(
            "⚠️ Please select two different languages."
        )

    else:

        with st.spinner(
            "🌍 AI is translating your text..."
        ):

            try:

                source_code = LANGUAGES[
                    source_language
                ]

                target_code = LANGUAGES[
                    target_language
                ]

                result = translate_text(
                    input_text,
                    source_code,
                    target_code
                )

                # SAVE EVERYTHING
                st.session_state.input_text = input_text

                st.session_state.translated_text = result

                st.session_state.source_language = source_language

                st.session_state.target_language = target_language

                st.session_state.translation_done = True

            except Exception as e:

                st.error(
                    f"❌ Translation error: {e}"
                )


# =========================================================
# OUTPUT SECTION
# =========================================================

if st.session_state.translation_done:

    original_text = st.session_state.input_text

    translated_text = st.session_state.translated_text

    source_language = st.session_state.source_language

    target_language = st.session_state.target_language


    # =====================================================
    # DIVIDER
    # =====================================================

    st.markdown(
        '<div class="gradient-divider"></div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # RESULT TITLE
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        '✨ Translation Result'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        f'{source_language} → {target_language}'
        '</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # INPUT + OUTPUT
    # =====================================================

    input_column, output_column = st.columns(
        2,
        gap="large"
    )


    # =====================================================
    # ORIGINAL INPUT
    # =====================================================

    with input_column:

        with st.container(border=True):

            st.markdown(
                f"### 📝 {source_language}"
            )

            st.caption(
                "Original Input Text"
            )

            st.text_area(
                "Original Input",
                value=original_text,
                height=240,
                disabled=True,
                key="original_result",
                label_visibility="collapsed"
            )


    # =====================================================
    # TRANSLATED OUTPUT
    # =====================================================

    with output_column:

        with st.container(border=True):

            st.markdown(
                f"### 🌍 {target_language}"
            )

            st.caption(
                "Translated Output"
            )

            st.text_area(
                "Translated Output",
                value=translated_text,
                height=240,
                key="translated_result",
                label_visibility="collapsed"
            )


    # =====================================================
    # COPY & DOWNLOAD
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        '📋 Copy & Save Translation'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Copy the translated text or download it as a text file.'
        '</div>',
        unsafe_allow_html=True
    )


    copy_column, download_column = st.columns(
        [1.5, 1]
    )


    # =====================================================
    # COPY
    # =====================================================

    with copy_column:

        st.markdown(
            "#### 📋 Copy Translation"
        )

        st.caption(
            "Use the copy icon in the top-right corner."
        )

        st.code(
            translated_text,
            language=None
        )


    # =====================================================
    # DOWNLOAD
    # =====================================================

    with download_column:

        st.markdown(
            "#### ⬇️ Save Translation"
        )

        st.caption(
            "Download the translated text."
        )

        st.write("")

        st.download_button(
            label="⬇️  DOWNLOAD TRANSLATION",
            data=translated_text,
            file_name="translated_text.txt",
            mime="text/plain",
            use_container_width=True
        )


    # =====================================================
    # STATISTICS
    # =====================================================

    st.divider()

    st.markdown(
        '<div class="section-title">'
        '📊 Translation Statistics'
        '</div>',
        unsafe_allow_html=True
    )


    source_words = len(
        original_text.split()
    )

    translated_words = len(
        translated_text.split()
    )

    source_characters = len(
        original_text
    )

    translated_characters = len(
        translated_text
    )


    metric1, metric2, metric3, metric4 = st.columns(4)


    with metric1:

        st.metric(
            "📝 Input Words",
            source_words
        )


    with metric2:

        st.metric(
            "🌍 Output Words",
            translated_words
        )


    with metric3:

        st.metric(
            "🔤 Input Characters",
            source_characters
        )


    with metric4:

        st.metric(
            "✨ Output Characters",
            translated_characters
        )


    # =====================================================
    # AI INFORMATION
    # =====================================================

    st.divider()

    st.markdown(
        '<div class="section-title">'
        '🚀 AI Translation Information'
        '</div>',
        unsafe_allow_html=True
    )


    info1, info2, info3 = st.columns(3)


    with info1:

        with st.container(border=True):

            st.markdown(
                "### 🌍 Multilingual AI"
            )

            st.write(
                "Translate text across multiple "
                "languages using one AI model."
            )

            st.caption(
                "NLLB-200 multilingual model"
            )


    with info2:

        with st.container(border=True):

            st.markdown(
                "### ⚡ Neural Translation"
            )

            st.write(
                "Uses a Transformer-based neural "
                "machine translation architecture."
            )

            st.caption(
                "AI-powered language conversion"
            )


    with info3:

        with st.container(border=True):

            st.markdown(
                "### 🔄 Easy Language Switching"
            )

            st.write(
                "Select source and target languages "
                "and translate with one click."
            )

            st.caption(
                "Simple interactive interface"
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer">'
    '🌍 <b>AI Language Translator</b>'
    '<br><br>'
    'Built with Streamlit • PyTorch • Hugging Face Transformers'
    '<br><br>'
    'Multilingual Translation Project • 2026'
    '</div>',
    unsafe_allow_html=True
)