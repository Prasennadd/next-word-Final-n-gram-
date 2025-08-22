import random
from collections import defaultdict


def tokenize(text):
    return text.lower().split()


# -----backbone
def build_ngram_model(tokens, n=3):
    model = defaultdict(list)
    for i in range(len(tokens) - n + 1):
        prefix = tuple(tokens[i:i + n - 1])
        next_word = tokens[i + n - 1]
        model[prefix].append(next_word)
    return model

# def predict_next(model, input_text, n=3):
#     words = tokenize(input_text)
#     if len(words) < n - 1:
#         return ''
#     prefix = tuple(words[-(n - 1):])
#     candidates = model.get(prefix, [])
#     return random.choice(candidates) if candidates else ''
def predict_next_all(model, input_text, n=3):
    words = tokenize(input_text)
    if len(words) < n - 1:
        return []
    prefix = tuple(words[-(n - 1):])
    candidates = model.get(prefix, [])
    return list(set(candidates))  # remove duplicates



def load_model(filepath, n=3):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    tokens = tokenize(text)
    return build_ngram_model(tokens, n)
