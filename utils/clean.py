import re
import emoji
import pandas as pd

slang_dict = {
    'wtf': 'what the fuck', 'lol': 'laughing out loud', 'fr': 'for real', 'tbh': 'to be honest',
    'fucking': 'fuckin', 'fuckinng': 'fuckin', 'ur': 'your', 'r': 'are',
    'omg': 'oh my god', 'dope': 'great', 'lit': 'great', 'nigga': 'nigga',
    'pussi': 'pussy', 'hoe': 'ho', 'fam': 'friends', 'dawg': 'friend',
    'stfu': 'shut up', 'yo': 'hey', 'vibin': 'vibing', 'chill': 'relax',
    'slaps': 'great', 'cap': 'lie', 'bet': 'okay'
}

def clean_text(text):
    if pd.isna(text) or not isinstance(text, str):
        return ''
    text = text.lower()
    text = emoji.demojize(text, delimiters=(' ', ' '))
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s!?]', '', text)
    for slang, full in slang_dict.items():
        text = re.sub(r'\b' + slang + r'\b', full, text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
