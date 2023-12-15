class DataAnalyzer:
    def __init__(self, dataset):
        self.dataset = dataset

    def get_dataset_info(self):
        print("Información del Dataset:")
        print(self.dataset.info())

    def check_missing_values(self):
        missing_values = self.dataset.isnull().sum()
        print("Valores Nulos en el Dataset:")
        print(missing_values)
