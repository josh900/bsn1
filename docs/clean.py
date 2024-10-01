import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def clean_text(text, min_word_length=3):
    lines = text.split('\n')
    cleaned_lines = []
    
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
    for line in lines:
        if line.startswith('#'):
            cleaned_lines.append(line)
            continue
        
        line = re.sub(r'http\S+|www\S+|https\S+', '', line, flags=re.MULTILINE)
        line = re.sub(r'[^a-zA-Z0-9\s]', '', line)
        line = line.lower()
        
        tokens = line.split()
        cleaned_tokens = [lemmatizer.lemmatize(token) for token in tokens 
                          if token not in stop_words and len(token) >= min_word_length]
        
        cleaned_lines.append(' '.join(cleaned_tokens))
    
    return '\n'.join(cleaned_lines)

# Read, clean, and write the text
with open('res.md', 'r', encoding='utf-8') as file:
    text = file.read()

cleaned_text = clean_text(text, min_word_length=4)

with open('cleaned_text.md', 'w', encoding='utf-8') as file:
    file.write(cleaned_text)

print("Text cleaning complete. Check 'cleaned_text.md' for the result.")