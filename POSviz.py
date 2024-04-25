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

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample text
text = "This is a sample sentence for POS tagging."

# Tokenize the text
tokens = word_tokenize(text)

# Perform POS tagging
pos_tags = pos_tag(tokens)

# Dictionary of POS tag abbreviations
pos_tag_abbreviations = {
    'CC': 'Coordinating conjunction',
    'CD': 'Cardinal number',
    'DT': 'Determiner',
    'EX': 'Existential there',
    'FW': 'Foreign word',
    'IN': 'Preposition or subordinating conjunction',
    'JJ': 'Adjective',
    'JJR': 'Adjective, comparative',
    'JJS': 'Adjective, superlative',
    'LS': 'List item marker',
    'MD': 'Modal',
    'NN': 'Noun, singular or mass',
    'NNS': 'Noun, plural',
    'NNP': 'Proper noun, singular',
    'NNPS': 'Proper noun, plural',
    'PDT': 'Predeterminer',
    'POS': 'Possessive ending',
    'PRP': 'Personal pronoun',
    'PRP$': 'Possessive pronoun',
    'RB': 'Adverb',
    'RBR': 'Adverb, comparative',
    'RBS': 'Adverb, superlative',
    'RP': 'Particle',
    'SYM': 'Symbol',
    'TO': 'to',
    'UH': 'Interjection',
    'VB': 'Verb, base form',
    'VBD': 'Verb, past tense',
    'VBG': 'Verb, gerund or present participle',
    'VBN': 'Verb, past participle',
    'VBP': 'Verb, non-3rd person singular present',
    'VBZ': 'Verb, 3rd person singular present',
    'WDT': 'Wh-determiner',
    'WP': 'Wh-pronoun',
    'WP$': 'Possessive wh-pronoun',
    'WRB': 'Wh-adverb'
}

# Display POS tags with their abbreviations
for tag in pos_tags:
    print(f"{tag[0]}: {tag[1]} ({pos_tag_abbreviations.get(tag[1], 'Unknown')})")
