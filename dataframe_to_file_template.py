import os
import pandas as pd
from abc import ABC, abstractmethod
from enums import FileMode, FileEncoding


class DataFrameToFileTemplate(ABC):
    """
    Classe base para exportar um DataFrame para um arquivo.
    """

    def export(self, df: pd.DataFrame, file_name: str, path_file: str = None, 
               file_mode: FileMode = FileMode.WRITE, encoding: FileEncoding = FileEncoding.UTF8):
        """
        Exporta o DataFrame, convertendo-o e salvando-o em arquivo.

        Args:
            df (pd.DataFrame): O DataFrame a ser exportado.
            file_name (str): Nome do arquivo (ex: 'output.json', 'output.csv').
            path_file (str): Caminho onde o arquivo será salvo. Se None, usa o diretório atual.
            file_mode (FileMode): Método de abertura do arquivo
            encoding (FileEncoding): Encoding do arquivo (Ex.: 'utf-8', 'latin-1'). Default: 'utf-8  
        """

        self._validate_dataframe(df)
        data = self.convert(df)
        file_path = self._resolve_path(file_name, path_file)
        self.save(data, file_path, file_mode, encoding)


    def _validate_dataframe(self, df: pd.DataFrame):
        """
        Metodo responsável por validar o dataframe 

        Args:
            df (pd.DataFrame): DataFrame pandas
        """

        if not isinstance(df, pd.DataFrame):
            raise TypeError("O argumento precisa ser um pandas DataFrame")
        else:
            print('DataFrame válido!')


    def _resolve_path(self, file_name: str, path_file: str = None) -> str:
        """
        Combina caminho e nome do arquivo. Se path_file não for fornecido, usa o diretório atual.

        Args:
            file_name (str): Nome do arquivo com a extensão (Ex.: output.json, output.csv)
            path_file (str): Caminho para salvar o arquivo
        """

        base_path = path_file or os.getcwd()
        return os.path.join(base_path, file_name)


    @abstractmethod
    def convert(self, df: pd.DataFrame):
        """
        Converte o arquivo DataFrame para o formato desejado

        Args:
            df (pd.DataFrame): DataFrame pandas
        """

        pass


    @abstractmethod
    def save(self, data, file_path: str = None, file_mode: FileMode = FileMode.WRITE, encoding: FileEncoding = FileEncoding.UTF8):
        """
        Salva o arquivo no caminho informado

        Args:
            data (any): Dados para salvar
            file_path (str): Caminho onde o arquivo será salvo. Se None, usa o diretório atual.
            file_mode (FileMode): Método de abertura do arquivo
            encoding (FileEncoding): Encoding do arquivo (Ex.: 'utf-8', 'latin-1'). Default: 'utf-8  
        """

        pass
