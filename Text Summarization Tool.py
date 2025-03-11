import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
import heapq
import sys

# Ensure necessary NLTK resources are downloaded
#nltk.download('punkt')
#nltk.download('stopwords')

def summarize_text(text, num_sentences=3):
    """Summarizes the input text using word frequency ranking."""
    try:
        text = text.strip()
        if not text:
            return "Error: No text provided for summarization."
        
        # Tokenize sentences
        sentences = sent_tokenize(text)
        if len(sentences) <= num_sentences:
            return text  # Return original text if too short
        
        # Tokenize words and calculate word frequencies
        words = word_tokenize(text.lower())
        stopwords = set(nltk.corpus.stopwords.words('english'))
        word_frequencies = Counter(w for w in words if w.isalnum() and w not in stopwords)
        
        # Score sentences based on word frequencies
        sentence_scores = {}
        for sentence in sentences:
            for word in word_tokenize(sentence.lower()):
                if word in word_frequencies:
                    sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]
        
        # Select top sentences for summary
        summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)
        return summary
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    print("\n===== AI Text Summarization Tool =====")
    try:
        user_text = input("Enter a long paragraph to summarize: ")
        if not user_text.strip():
            print("Error: Input text cannot be empty.")
            sys.exit(1)
        
        num_sentences = input("Enter the number of sentences for the summary (default is 3): ")
        num_sentences = int(num_sentences) if num_sentences.isdigit() else 3
        
        summary = summarize_text(user_text, num_sentences)
        print("\n===== Generated Summary =====")
        print(summary)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")