import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import ast

class DatasetPreparation:
    def __init__(self, dataset):
        self.dataset = dataset

    def convert_embeddings_to_numeric(self, embedding_columns):
        for column in embedding_columns:
            self.dataset[column] = self.dataset[column].apply(self._convert_embedding)

    @staticmethod
    def _convert_embedding(embedding_str):
        try:
            embedding_list = ast.literal_eval(embedding_str)
            return np.array(embedding_list)
        except ValueError:
            return np.array([])

    def normalize_embeddings(self, embedding_columns):
        scaler = StandardScaler()
        for column in embedding_columns:
            valid_embeddings = [emb for emb in self.dataset[column] if emb.size > 0]
            if valid_embeddings:
                scaled_embeddings = scaler.fit_transform(np.stack(valid_embeddings))
                self.dataset[column] = list(scaled_embeddings)

    def split_dataset(self, test_size=0.3, val_size=0.5):
        train, test = train_test_split(self.dataset, test_size=test_size, random_state=42)
        val, test = train_test_split(test, test_size=val_size, random_state=42)
        return train, val, test
