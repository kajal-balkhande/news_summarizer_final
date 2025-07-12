from transformers import pipeline
import torch 

# Load the Hugging Face summarization pipeline once
summarizer = pipeline("summarization",model="facebook/bart-large-cnn")

def summarize_text(text, max_length=120, min_length=30):
    """
    Summarizes a given input text using a pretrained model.
    """
    try:
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Error during summarization: {e}"