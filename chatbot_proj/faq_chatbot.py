import spacy

# Load SpaCy English language model
nlp = spacy.load("en_core_web_sm")

# Sample FAQ data
faq_data = [
    {"question": "What is your return policy?", "answer": "You can return any item within 30 days of purchase."},
    {"question": "How can I track my order?", "answer": "You can track your order using the tracking link sent to your email."},
    {"question": "Do you ship internationally?", "answer": "Yes, we ship to most countries worldwide."},
    {"question": "How can I contact customer support?", "answer": "You can contact customer support via email at support@example.com."},
    # Add more FAQs as needed
]

def preprocess_text(text):
    """
    Preprocess the text by tokenizing and lemmatizing.
    """
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

def find_answer(user_input, faq_data):
    """
    Find the best answer for the user input from the FAQ data.
    """
    processed_input = preprocess_text(user_input)
    best_match = None
    highest_similarity = 0.0
    
    for faq in faq_data:
        processed_question = preprocess_text(faq["question"])
        similarity = nlp(processed_input).similarity(nlp(processed_question))
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = faq
    
    return best_match["answer"] if best_match else "I'm sorry, I don't have an answer for that."

def main():
    print("Welcome! I'm FAQ Chatbot. Ask me anything about our products or policies.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        answer = find_answer(user_input, faq_data)
        print(f"FAQ Bot: {answer}")

if __name__ == "__main__":
    main()
