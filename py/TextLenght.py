class TextLengthAdder:
    def __init__(self, dataset):
        self.dataset = dataset

    def add_text_length_columns(self, question_col, answer_col):
        self.dataset['question_length'] = self.dataset[question_col].apply(len)
        self.dataset['answer_length'] = self.dataset[answer_col].apply(len)
