import nltk
import spacy

# Verify NLTK installation
nltk.download('punkt')

# Verify SpaCy installation and language model
nlp = spacy.load("en_core_web_sm")
print("Installation successful!")
