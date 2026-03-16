# 🎙️ Grammar Scoring Engine from Voice Samples

An end-to-end AI system that evaluates **spoken English grammar** by converting audio to text, detecting grammatical errors using NLP, generating a normalized score, and mapping it to **CEFR proficiency levels**.

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B)](https://grammar-scoring-engine-bjzcgy4bkvfwi36ah3cmwn.streamlit.app)
[![Python](https://img.shields.io/badge/Python-100%25-blue)](https://www.python.org/)
[![Deployed](https://img.shields.io/badge/Deployment-Streamlit_Cloud-success)](https://streamlit.io/)

---

## 🔗 Live Demo

👉 **[Try it live →](https://grammar-scoring-engine-bjzcgy4bkvfwi36ah3cmwn.streamlit.app)**

Upload any English `.wav` audio file and get instant grammar feedback!

---

## 🎯 Problem Statement

Assessing spoken grammar is critical for:
- **Language learning platforms** (Duolingo, IELTS prep)
- **Hiring tools** (spoken English screening)
- **Educational assessments** (CEFR-based evaluation)

This project builds a lightweight, cloud-deployable grammar evaluation pipeline that works on real-world audio input — no Java, no heavy dependencies.

---

## 🧠 System Architecture
```
Audio Input (.wav)
        │
        ▼
Speech-to-Text (Google Speech API)
        │
        ▼
Grammar Error Detection (LanguageTool NLP API)
        │
        ▼
Score Normalization (0–100)
        │
        ▼
CEFR Level Mapping (A1 → C2)
        │
        ▼
Streamlit Web Interface
```

---

## ⚙️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.10+ |
| Speech-to-Text | SpeechRecognition (Google Speech API) |
| Grammar Analysis | LanguageTool Public API (cloud-safe, Java-free) |
| UI & Deployment | Streamlit + Streamlit Cloud |
| Audio Samples | WAV format input |

---

## 📊 Grammar Scoring Methodology

1. Spoken audio is **transcribed** into text using Google Speech API
2. Grammar errors are **detected** using rule-based NLP (LanguageTool)
3. **Error density** is computed against total word count
4. A **normalized score (0–100)** is generated
5. Score is **mapped to CEFR proficiency level**

### 🎯 CEFR Score Mapping

| Score Range | CEFR Level | Description |
|---|---|---|
| 90 – 100 | C1 / C2 | Advanced / Mastery |
| 75 – 89 | B2 | Upper Intermediate |
| 60 – 74 | B1 | Intermediate |
| 40 – 59 | A2 | Elementary |
| < 40 | A1 | Beginner |

---

## ✨ Features

- 🎤 Upload any English `.wav` audio file
- 📝 Real-time speech-to-text transcription
- 🔍 Automatic grammar error detection
- 📊 Normalized grammar score (0–100)
- 🏆 CEFR proficiency level estimation
- ✅ Highlighted error details
- ☁️ Fully cloud-deployed — works in browser, no setup needed

---

## 🚀 Run Locally

### Step 1 — Clone the repo
```bash
git clone https://github.com/M1325-source/grammar-scoring-engine.git
cd grammar-scoring-engine
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Run the app
```bash
streamlit run app.py
```

Open **http://localhost:8501** in your browser.

---

## 📁 Project Structure
```
grammar-scoring-engine/
│
├── app.py                  ← Streamlit web app (main entry)
├── train.py                ← Model training / scoring logic
├── requirements.txt        ← Python dependencies
├── audio_samples/          ← Sample .wav files for testing
└── README.md
```

---

## 🔍 Key Design Decisions

- **Avoided Java-based LanguageTool** — used REST API instead for Streamlit Cloud compatibility
- **Dataset-agnostic pipeline** — works on any real-world English audio
- **Modular architecture** — each stage (STT, NLP, scoring) is independent
- **Cloud-first approach** — no local server or runtime dependencies needed

---

## 🔮 Future Enhancements

- ML-based grammar scoring model (regression on CEFR labels)
- Pronunciation & fluency analysis
- Multi-language support
- Confidence & coherence metrics
- Real-time microphone recording
- Batch audio processing

---

## 👩‍💻 Author

**Manisha Priya**
AI/ML Engineer | NLP Enthusiast

- 🐙 GitHub: [@M1325-source](https://github.com/M1325-source)
- 📧 Email: manishapriya1325@gmail.com

---

> Built as part of an AI research assessment — demonstrates real-world NLP pipeline design, speech processing, and cloud deployment best practices.

⭐ **If you found this useful, please star the repo!**
