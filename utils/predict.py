from .clean import clean_text
from .model_loader import tokenizer, model
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

max_length = 30
vocab_size = 20000

def predict_text(text):
    cleaned_text = clean_text(text)
    sequence = tokenizer.texts_to_sequences([cleaned_text])
    padded = np.clip(pad_sequences(sequence, maxlen=max_length, padding='post', truncating='post'), 0, vocab_size - 1)

    probs = model.predict(padded, verbose=0)[0]
    class_names = ['Hate Speech', 'Offensive', 'Neither']
    pred_class = class_names[np.argmax(probs)]
    confidence = probs[np.argmax(probs)]

    return {
        'cleaned': cleaned_text,
        'predicted_class': pred_class,
        'confidence': float(confidence),
        'scores': dict(zip(class_names, map(float, probs)))
    }
