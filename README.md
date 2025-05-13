 AI-Powered Medical Report Summarization & Fake News Detection
An interactive web application that combines AI-powered summarization of medical reports and fake health news detection to enhance the user experience and healthcare content verification.

Built with Streamlit, Hugging Face Transformers, and Python, this project leverages T5 for medical report summarization and BART for fake news detection.

🚀 Demo Link
Check out the live demo of this project here.

🚀 Features
🧠 Summarize Medical Reports

Input detailed medical documents and get a summarized version with essential information.

⚡ Fake Health News Detection

Classify health-related news articles as Real or Fake using advanced NLP models.

🔍 Confidence Scores

Provides a confidence score for both the summarization and the fake news classification.

🧾 Interactive Interface

Simple, user-friendly Streamlit UI to easily interact with the app.

🛠️ Tech Stack
Layer	Technology/Tool
Frontend	Streamlit
NLP Models	Hugging Face Transformers (T5, BART)
Environment	Python, Virtual Environment

🚀 Setup Instructions
Step 1 – Clone the Repository
bash
Copy code
git clone https://github.com/your-username/AI-Medical-Report-Summarization.git
cd AI-Medical-Report-Summarization
Step 2 – Create & Activate a Virtual Environment
For Windows:

bash
Copy code
python -m venv .venv
.venv\Scripts\activate
For macOS/Linux:

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
After running this, you can view the app at http://localhost:8501.

🎯 Example Use Cases
1. Medical Report Summarization
Input: Long, detailed medical reports.

Output: Concise summaries with key medical insights.

2. Fake Health News Detection
Input: Health-related news articles.

Output: Classification as REAL or FAKE, along with confidence scores.

📞 Contact
Author: Sanskriti Gupta

