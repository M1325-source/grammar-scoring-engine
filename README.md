\# 🎙️ Grammar Scoring Engine from Voice Samples



An end-to-end AI system that evaluates the grammatical quality of spoken English by converting speech to text, detecting grammatical errors, and generating a normalized score with CEFR proficiency mapping.



---

\## 🚀 Live Demo

🔗 \*\*Streamlit App:\*\* https://grammar-scoring-engine-bjzcgy4bkvfwi36ah3cmwn.streamlit.app  

🔗 \*\*GitHub Repo:\*\* https://github.com/M1325-source/grammar-scoring-engine



---



\## 📌 Problem Statement

Assessing spoken grammar is essential for language learning platforms, assessments, and hiring tools. This project demonstrates a lightweight, scalable grammar evaluation pipeline that works on real-world audio input.



---



\## 🧠 System Architecture



Audio Input (.wav)

↓

Speech-to-Text Conversion

↓

Grammar Error Detection (NLP)

↓

Score Normalization

↓

CEFR Level Mapping

↓

Interactive Web Interface



yaml

Copy code



---



\## ⚙️ Tech Stack

\- \*\*Python\*\*

\- \*\*SpeechRecognition\*\* (Google Speech API)

\- \*\*LanguageTool Public API\*\* (Java-free, cloud-safe)

\- \*\*Streamlit\*\* (UI \& Deployment)

\- \*\*GitHub + Streamlit Cloud\*\* (CI/CD)



---



\## 📊 Grammar Scoring Methodology

\- Spoken audio is transcribed into text.

\- Grammar errors are detected using rule-based NLP.

\- Error density is used to compute a normalized score (0–100).

\- The score is mapped to \*\*CEFR proficiency levels\*\*.



\### 🎯 CEFR Mapping

| Score Range | CEFR Level |

|------------|-----------|

| 90–100 | C1 / C2 (Advanced) |

| 75–89 | B2 (Upper Intermediate) |

| 60–74 | B1 (Intermediate) |

| 40–59 | A2 (Elementary) |

| < 40 | A1 (Beginner) |



---



\## ✨ Features

\- Upload \*\*any English audio (.wav)\*\*

\- Real-time grammar analysis

\- Highlighted grammatical errors

\- CEFR proficiency estimation

\- Fully cloud-deployed (no Java dependency)



---



\## ☁️ Deployment

The application is deployed on \*\*Streamlit Cloud\*\* and supports real-time inference without external runtime dependencies like Java.



---



\## 🔍 Design Decisions

\- Avoided Java-based tools to ensure cloud compatibility.

\- Built a dataset-agnostic pipeline to support real-world usage.

\- Modular architecture for easy future extensions.



---



\## 🔮 Future Enhancements

\- ML-based grammar scoring model

\- Pronunciation \& fluency analysis

\- Multi-language support

\- Confidence \& coherence metrics



---



\## 👩‍💻 Author

\*\*Manisha Priya\*\*  

AI / ML Enthusiast | Research Intern Applicant  



---



> This project was developed as part of an AI research assessment and reflects real-world engineering decisions for robustness and deployment.

