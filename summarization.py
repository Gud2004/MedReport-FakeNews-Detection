from transformers import pipeline

# Initialize the summarization pipeline using T5-base
summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base")

def summarize_text(text, max_length=150, min_length=40):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']


# def summarize_text(text, level="medium"):
#     if level == "short":
#         return "Short summary: Key highlights only."
#     elif level == "medium":
#         return "Medium summary: Balanced summary with essential details."
#     elif level == "detailed":
#         return "Detailed summary: In-depth explanation with medical terms."
#     else:
#         return "Invalid selection."
