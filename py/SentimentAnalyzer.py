from textblob import TextBlob

class SentimentAnalyzer:
    def __init__(self, dataset):
        self.dataset = dataset

    def add_polarity_columns(self, question_col, answer_col):
        self.dataset['question_polarity'] = self.dataset[question_col].apply(self._calculate_polarity)
        self.dataset['answer_polarity'] = self.dataset[answer_col].apply(self._calculate_polarity)

    @staticmethod
    def _calculate_polarity(text):
        return TextBlob(text).sentiment.polarity
