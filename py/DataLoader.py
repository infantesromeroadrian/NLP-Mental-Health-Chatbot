import pandas as pd

class DatasetLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_dataset(self):
        try:
            data = pd.read_csv(self.file_path)
            return data
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
            return None

    def preview_dataset(self, num_rows=5):
        data = self.load_dataset()
        if data is not None:
            print(data.head(num_rows))
        else:
            print("No hay datos para mostrar.")
