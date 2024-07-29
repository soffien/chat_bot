import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class SimpleChatbotModel:
    def __init__(self):
        self.qa_dict = {
            "hi": "Hello! How can I help you today?",
            "what is your name?": "I am a chatbot created to assist you.",
            "how are you?": "I'm just a bot, but I'm here to help!",
            "bye": "Goodbye! Have a great day!"
        }
        self.questions = list(self.qa_dict.keys())
        self.responses = list(self.qa_dict.values())
        self.vectorizer = CountVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

    def preprocess(self, text):
        text = text.lower()
        text = re.sub(r'\W+', ' ', text)
        return text

    def predict(self, message):
        preprocessed_message = self.preprocess(message)
        message_vector = self.vectorizer.transform([preprocessed_message])
        similarities = cosine_similarity(message_vector, self.question_vectors)
        best_match_index = np.argmax(similarities)
        return self.responses[best_match_index]
