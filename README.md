# 🌍 AI-Language_Text_Translator
🌍 AI Language Translator is a multilingual translation application built using Streamlit, PyTorch, and Hugging Face Transformers. Powered by the NLLB-200 model, it translates text across 40+ languages and offers language switching, translation statistics, copy and download options, and GPU/CPU support through an interactive dashboard.

# 🌍 AI Language Translator — Multilingual Translation System

## 📌 Project Overview

AI Language Translator is an AI-powered multilingual translation application built using Streamlit, PyTorch, and Hugging Face Transformers. It uses the NLLB-200 multilingual model to translate text between 40 languages through an interactive dashboard, with language selection, translation results, statistics, and download functionality.

## 🎯 Project Objectives

- 🌐 Translate text between multiple languages using AI.
- 🤖 Implement Transformer-based neural machine translation.
- 🔄 Provide an easy-to-use language selection and switching system.
- 📊 Display translation statistics for input and output text.
- 📋 Enable users to copy and download translated text.
- ⚡ Support GPU and CPU execution.

## ✨ Key Features

- 🌍 **Multilingual Translation:** Translate text between 40 supported languages.
- 🧠 **AI-Powered Model:** Uses the NLLB-200 multilingual translation model.
- 🔄 **Language Switching:** Swap source and target languages with one click.
- 📝 **Text Input:** Enter or paste text for translation.
- 📊 **Translation Statistics:** Display input/output word and character counts.
- 📋 **Copy Support:** Copy the generated translation from the result section.
- ⬇️ **Download Translation:** Save translated text as a `.txt` file.
- 🎨 **Interactive Dashboard:** Modern Streamlit interface with a dark gradient design.
- ⚡ **GPU/CPU Support:** Automatically selects CUDA when available or uses the CPU.
- 💬 **Side-by-Side Results:** View the original and translated text together.

## 🛠️ Technologies Used

1. 🐍 Python
2. 🧠 Artificial Intelligence
3. 📝 Natural Language Processing (NLP)
4. 🤗 Hugging Face Transformers
5. 🌐 NLLB-200
6. 🔥 PyTorch
7. 🖥️ Streamlit
8. 📊 NumPy
9. 📚 Hugging Face Datasets
10. ⚙️ Hugging Face Tokenizers
11. ☁️ Google Colab
12. 📏 SacreBLEU

## 🧠 Model Architecture

1. 🤖 **Model Name:** NLLB-200 Distilled 600M
2. 📦 **Model Checkpoint:** `facebook/nllb-200-distilled-600M`
3. 🏗️ **Model Type:** Multilingual Sequence-to-Sequence Transformer
4. 🌐 **Task:** Neural Machine Translation
5. 🔥 **Framework:** PyTorch
6. 🤗 **Model Library:** Hugging Face Transformers
7. 🔤 **Tokenization:** NLLB-200 Tokenizer
8. ⚡ **Inference:** Autoregressive text generation
9. 💻 **Execution Device:** CUDA GPU or CPU
10. 🖥️ **Application Framework:** Streamlit

![ml](https://github.com/rushikeshwalode06-cod/AI-Language_Text_Translator/blob/main/Language_Translator_model_image.png?raw=true)

## 🌐 Supported Languages

The application includes 40 languages, including:

- 🇬🇧 English
- 🇮🇳 Hindi
- 🇮🇳 Marathi
- 🇫🇷 French
- 🇩🇪 German
- 🇪🇸 Spanish
- 🇮🇹 Italian
- 🇵🇹 Portuguese
- 🇷🇺 Russian
- 🇨🇳 Chinese (Simplified)
- 🇯🇵 Japanese
- 🇰🇷 Korean
- 🇸🇦 Arabic
- 🇮🇳 Bengali
- 🇮🇳 Gujarati
- 🇮🇳 Punjabi
- 🇮🇳 Tamil
- 🇮🇳 Telugu
- 🇮🇳 Kannada
- 🇮🇳 Malayalam
- 🇵🇰 Urdu
- 🇳🇵 Nepali
- 🇳🇱 Dutch
- 🇹🇷 Turkish
- 🇻🇳 Vietnamese
- 🇹🇭 Thai
- 🇵🇱 Polish
- 🇺🇦 Ukrainian
- 🇬🇷 Greek
- 🇷🇴 Romanian
- 🇸🇪 Swedish
- 🇩🇰 Danish
- 🇫🇮 Finnish
- 🇨🇿 Czech
- 🇭🇺 Hungarian
- 🇮🇱 Hebrew
- 🇮🇷 Persian
- 🇰🇪 Swahili
- 🇮🇩 Indonesian
- 🇲🇾 Malay
- 🇵🇭 Filipino

## ⚙️ Project Workflow

1. 📥 **Model Loading:** Load the pretrained NLLB-200 model and tokenizer from Hugging Face.
2. 🌐 **Language Selection:** Select the source and target languages.
3. 📝 **Text Input:** Enter or paste the text to translate.
4. 🔤 **Language Mapping:** Map the selected languages to their corresponding NLLB language codes.
5. 🧩 **Tokenization:** Convert the input text into model-compatible token IDs.
6. ⚡ **Device Processing:** Move the tokenized input to the available GPU or CPU.
7. 🤖 **Translation Generation:** Generate translated tokens using the selected target-language code.
8. 📄 **Text Decoding:** Convert the generated tokens into readable text.
9. 📊 **Result Display:** Display the original and translated text side by side.
10. 💾 **Export and Statistics:** Provide copy support, text download, and translation statistics.

## 🔬 Translation Process

1. 📝 **Text Input:** The user enters text in the source language.
2. 🔤 **Tokenization:** The tokenizer converts the text into numerical representations.
3. 🧠 **Model Processing:** The model processes the input sequence.
4. 🌐 **Target Language Selection:** The target-language token ID guides the model toward the selected output language.
5. 🤖 **Translation Generation:** The model generates the translated sequence.
6. 📄 **Text Decoding:** The tokenizer converts the generated tokens into readable text.
7. 🖥️ **Result Display:** Streamlit displays the translated text and related statistics.

## 🖥️ Application Interface

The Streamlit application includes:

1. 🎨 A modern AI translator dashboard.
2. ⚙️ A sidebar displaying model and device information.
3. 🌐 Source and target language selection.
4. 🔄 A language-swap button.
5. 📝 A text input area.
6. 🚀 A Translate Now button.
7. 📄 Side-by-side original and translated text panels.
8. 📋 A copy-friendly translation output.
9. ⬇️ A translation download button.
10. 📊 Input and output word and character statistics.

## 📊 Translation Statistics

After translation, the application calculates:

- 📝 **Input Words:** Number of words in the original text.
- 🌍 **Output Words:** Number of words in the translated text.
- 🔤 **Input Characters:** Number of characters in the original text.
- ✨ **Output Characters:** Number of characters in the translated text.

These statistics help users compare the original and translated text lengths.

## 🧪 Model Training Experiment

The accompanying Google Colab notebook also contains an English-to-French translation fine-tuning experiment.

1. 📚 **Training Dataset:** `dany0407/my_dataset_en_fr`
2. 🧠 **Base Model:** `Helsinki-NLP/opus-mt-en-fr`
3. 🌐 **Task:** English-to-French machine translation
4. ⚙️ **Training Approach:** Supervised fine-tuning
5. 📊 **Dataset Split:** 90% training and 10% validation
6. 🔢 **Maximum Sequence Length:** 128 tokens
7. 🔄 **Training Epochs:** 3
8. 📏 **Evaluation Metric:** SacreBLEU
9. 🤗 **Training Framework:** Hugging Face Transformers
10. 🏋️ **Trainer:** `Seq2SeqTrainer`
11. 💾 **Training Output Checkpoint:** `dany0407/dany-en-to-fr`

**Note:** This notebook experiment is separate from the Streamlit application's NLLB-200 inference model. The app loads `facebook/nllb-200-distilled-600M`, while the notebook demonstrates fine-tuning an English-to-French model.

## ⚠️ Limitations

1. 🌐 Translation quality may vary depending on the language pair and input text.
2. 📚 Low-resource languages may produce less accurate translations.
3. ✂️ The application truncates input to a maximum of 512 tokens, so longer text may be cut off.
4. 🧠 Generated translations may contain grammatical errors or lose some context.
5. 💻 Running the model on a CPU may be slower than using a compatible GPU.
6. 🌍 Only the 40 languages configured in the application are selectable.
7. 📏 Word and character statistics measure text length, not translation accuracy.
8. 🧪 Translation quality should be evaluated with suitable test data before production use.

## 🔮 Future Scope

1. 🚀 Improve translation quality through model fine-tuning and evaluation.
2. 📄 Add document translation for PDF, DOCX, and TXT files.
3. 🎙️ Integrate speech-to-text and text-to-speech translation.
4. 🖼️ Add OCR to translate text extracted from images.
5. 💬 Introduce real-time conversation translation.
6. 🌐 Expand the supported language list.
7. 📊 Add BLEU and other suitable translation evaluation metrics.
8. ☁️ Deploy the application on a scalable cloud platform.
9. 📱 Optimize the interface for mobile devices.
10. 🗂️ Add translation history and saved translations.

## 🏁 Conclusion

AI Language Translator demonstrates how multilingual Transformer models can be integrated into an interactive web application. By combining NLLB-200, PyTorch, Hugging Face Transformers, and Streamlit, the project provides a convenient way to translate text across multiple languages. Its language selection, translation output, statistics, and download features make it a useful foundation for further development of AI-powered language tools.

![ml](https://github.com/rushikeshwalode06-cod/AI-Language_Text_Translator/blob/main/Language_Translator_image.png?raw=true)
