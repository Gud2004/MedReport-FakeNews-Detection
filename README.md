
📄 AI-Powered Medical Report Summarization & Fake News Detection
An interactive web application that combines AI-based summarization of medical reports with fake health news detection. Built using Streamlit, Hugging Face Transformers, and Python, it enhances user experience and healthcare content verification.

🚀 Live Demo
🚀 Features
🧠 Summarize Medical Reports
Generate concise, meaningful summaries from lengthy medical documents using T5.

⚡ Fake Health News Detection
Classify health-related news as Real or Fake using BART.

🔍 Confidence Scores
Displays the confidence level of both summarization and classification.

🧾 Interactive Interface
Clean, responsive UI built with Streamlit.

🛠️ Tech Stack
Layer	Technology/Tool
Frontend	Streamlit
NLP Models	Hugging Face Transformers (T5, BART)
Environment	Python, Virtual Environment

⚙️ Setup Instructions
Step 1 – Clone the Repository

bash
Copy code
git clone https://github.com/your-username/AI-Medical-Report-Summarization.git
cd AI-Medical-Report-Summarization
Step 2 – Create & Activate Virtual Environment

Windows

bash
Copy code
python -m venv .venv
.venv\Scripts\activate
macOS/Linux

bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
Step 3 – Install Dependencies

bash
Copy code
pip install -r requirements.txt
Step 4 – Run the Application

bash
Copy code
streamlit run app.py
Access the app at: http://localhost:8501

🎯 Example Use Cases
Medical Report Summarization
🔹 Input: Long clinical reports
🔹 Output: Short, insightful summaries

Fake Health News Detection
🔹 Input: Health-related article
🔹 Output: Classification as REAL or FAKE with confidence

👩‍💻 Author
Sanskriti Gupta

