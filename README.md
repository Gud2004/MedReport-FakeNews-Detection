# 🧠 AI-Powered Medical Report Summarization & Fake News Detection

An interactive web application that combines **AI-based summarization of medical reports** with **fake health news detection**. Built using **Streamlit**, **Hugging Face Transformers**, and **Python**, the app provides an enhanced user experience in summarizing clinical documents and verifying healthcare information authenticity.

## 🚀 Live Demo
👉 [(https://medreport-fakenews-detection-jvhrdhlujpsyptmrvchcpw.streamlit.app/)]

---

## 🚀 Features

### 🧾 Summarize Medical Reports
- Generate **concise and insightful summaries** from lengthy medical documents using the **T5 transformer model**.

### ⚡ Fake Health News Detection
- Detect and classify health-related news articles as **REAL** or **FAKE** using the **BART model**.

### 🔍 Confidence Scores
- Visual representation of model **confidence levels** for both summarization and classification outputs.

### 🖥️ Interactive Interface
- User-friendly, **clean and responsive UI** built using **Streamlit**.

---

## 🛠️ Tech Stack

| Layer        | Technology/Tool                            |
|--------------|---------------------------------------------|
| Frontend     | Streamlit                                  |
| NLP Models   | Hugging Face Transformers (T5, BART)       |
| Environment  | Python, Virtual Environment                |

---
### ⚙️ Setup Instructions

```bash
# Step 1 – Clone the Repository
git clone https://github.com/your-username/AI-Medical-Report-Summarization.git
cd AI-Medical-Report-Summarization

# Step 2 – Create & Activate Virtual Environment

# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# Step 3 – Install Dependencies
pip install -r requirements.txt

# Step 4 – Run the Application
streamlit run app.py

# Access the app at:
# http://localhost:8501


🎯 Example Use Cases
🩺 Medical Report Summarization
Input: Long clinical notes, discharge summaries

Output: Short, clear summaries useful for quick review

📰 Fake Health News Detection
Input: Health-related articles or claims

Output: Classified as REAL or FAKE with confidence percentag
