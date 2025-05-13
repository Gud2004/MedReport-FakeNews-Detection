# translation.py using deep_translator
from deep_translator import GoogleTranslator

def translate_text(text, dest='en'):
    try:
        # deep_translator automatically detects the source language
        translation = GoogleTranslator(source='auto', target=dest).translate(text)
        return translation
    except Exception as e:
        return f"Translation error: {e}"

