import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "This is a sample sentence for POS tagging."

# Process the text using spaCy
doc = nlp(text)

# Display POS tags with their abbreviations and descriptions
for token in doc:
    print(f"{token.text}: {token.pos_} ({spacy.explain(token.pos_)})")
