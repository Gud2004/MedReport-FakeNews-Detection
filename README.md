📄 AI-Powered PDF Chatbot

An interactive PDF-based chatbot application that allows users to ask questions about uploaded documents. Built with LangChain, Streamlit, and LLMs like Llama 3, it uses vector embeddings to understand and answer queries based on document context.

🚀 Demo Link
Check out the live demo of this project here

🚀 Features
🧠 Ask questions about the content of one or more PDF files

⚡ Fast responses using LangChain and Groq's Llama 3 API

🔍 Context-aware answers powered by Retrieval-Augmented Generation (RAG)

🧾 Shows document source and page references

📂 Upload multiple PDFs and process them with real-time feedback

🧠 Uses Google Generative AI for embeddings

🗂️ Maintains full chat history during the session

🛠️ Tech Stack
Layer	Technology/Tool
Frontend	Streamlit
Backend	LangChain, FAISS, PyPDFLoader
Embeddings	Google Generative AI Embeddings
LLM	ChatGroq (Llama3-8b-8192)
Environment	Python, .env, tempfile, os

🚀 Setup Instructions
Step 1 – Clone the Repository

bash
Copy code
git clone https://github.com/Gud2004/project12.git
cd project12
Step 2 – Create & Activate a Virtual Environment

For Windows:

bash
Copy code
python -m venv venv
venv\Scripts\activate
For macOS/Linux:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Step 3 – Install Dependencies

bash
Copy code
pip install -r requirements.txt
Step 4 – Set Up Environment Variables

GOOGLE_API_KEY=your_google_api_key

GROQ_API_KEY=your_groq_api_key

Step 5 – Run the Application

bash
Copy code
streamlit run app.py
✍️ Author: Sanskriti Gupta
