import random
import json
import pickle
import numpy as np
import re

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow import keras


lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents2.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

try:
    model = keras.models.load_model('chatbotmodel.h5')
except:
    print("Failed to load model")


ERROR_THRESHOLD = 0.25

# load the pre-trained GloVe word embeddings
embeddings_index = {}
with open('glove.6B.300d.txt', encoding='utf8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs

# create a weight matrix for words in training docs
embedding_matrix = np.zeros((len(words), 300))
for i, word in enumerate(words):
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        embedding_matrix[i] = embedding_vector


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)


def predict_class(sentence, model):
    if not model:
        return [{'intent': 'error', 'probability': '1.0'}]
    bow = bag_of_words(sentence, words, show_details=False)
    res = model.predict(np.array([bow]))[0]
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []

    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    result = "Sorry, can't understand you, please give me more info"
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


print("Go! Bot is running!")

while True:

    message = input("")
    if re.search(r'\b(goodbye|bye|see you later)\b', message, re.IGNORECASE):
        print("Goodbye!")
        break
    ints = predict_class(message, model)
    if len(ints) > 0:
        res = get_response(ints, intents)
        print(res)
    else:
        print("Sorry, I didn't understand that")
