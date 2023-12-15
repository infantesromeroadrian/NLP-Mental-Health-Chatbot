import re
import pandas as pd

class DataPreprocessor:
    def __init__(self, dataset):
        self.dataset = dataset

    def clean_text(self, column):
        self.dataset[column] = self.dataset[column].apply(self._clean_text_helper)

    @staticmethod
    def _clean_text_helper(text):
        text = re.sub('[^A-Za-z]+', ' ', text)
        text = text.lower()
        text = text.strip()
        return text
