# # fake_news_detection.py
from transformers import pipeline

# Initialize the zero-shot classification pipeline using facebook/bart-large-mnli.
# This model is commonly used for zero-shot tasks.
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")


def detect_fake_news(text):
    """
    Detects whether the provided text is classified as fake or real using zero-shot classification.

    Args:
        text (str): The text (e.g., a news article) to classify.

    Returns:
        tuple: A tuple containing:
            - predicted_label (str): The predicted label ("FAKE" or "REAL").
            - confidence (float): The confidence score for the prediction.
    """
    # Candidate labels for classification
    candidate_labels = ["fake", "real"]

    try:
        # Run the classifier on the input text
        result = classifier(text, candidate_labels)
        # Extract the most likely label and its confidence score
        predicted_label = result["labels"][0]
        confidence = result["scores"][0]
        return predicted_label.upper(), confidence
    except Exception as e:
        # Return a default value or raise the error after logging
        raise RuntimeError(f"Error during fake news detection: {e}")


#
# import random
#
# def detect_fake_news(text):
#     confidence = random.randint(70, 99)  # Simulated confidence score
#     result = "FAKE" if confidence > 50 else "REAL"
#     return result, confidence

# from transformers import pipeline
#
# def initialize_classifier():
#     """
#     Initializes the text classification pipeline with a more suitable model.
#     """
#     try:
#         classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
#         return classifier
#     except Exception as e:
#         raise RuntimeError(f"Error loading the model: {e}")
#
# # Initialize model
# classifier = initialize_classifier()
#
# def detect_fake_news(text):
#     """
#     Detects whether the provided text is classified as fake or real.
#
#     Args:
#         text (str): The text (e.g., a news article) to classify.
#
#     Returns:
#         tuple: (predicted_label, confidence_score)
#     """
#     try:
#         result = classifier(text)
#         predicted_label = "FAKE" if result[0]["label"] == "NEGATIVE" else "REAL"
#         confidence = result[0]["score"]
#         return predicted_label, confidence
#     except Exception as e:
#         raise RuntimeError(f"Error during fake news detection: {e}")
