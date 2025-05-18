import pandas as pd
from abc import ABC, abstractmethod


class Converter(ABC):
    """
    Classe responsável por implementar os métodos de conversão de dataframes
    """
    @abstractmethod
    def convert(self, df: pd.DataFrame):
        """
        Converte o arquivo DataFrame para o formato desejado

        Args:
            df (pd.DataFrame): DataFrame pandas
        """

        pass
