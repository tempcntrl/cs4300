# Function to get number of words
import string

def CountWords(filePath):
    with open(filePath, 'r') as f:
        text = f.read()
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)
    words = cleaned_text.split()
    return len(words)
