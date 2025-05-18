import json
import pandas as pd
from utils.enums import FileEncoding, FileMode
from interface.converter_strategy import Converter
from interface.saver_strategy import Saver
from core.exporter import DataFrameToExporter


class JsonConverter(Converter):

    def convert(self, df: pd.DataFrame):
        """
        Realiza a conversão do dataframe para uma lista de dicionários
        """
        print('DataFrame convertido com sucesso!')
        return df.to_dict(orient='records')


class JsonSaver(Saver):

    def save(self, data, file_path: str = None, file_mode: FileMode = FileMode.WRITE, encoding: FileEncoding = FileEncoding.UTF8):
            """
            Método para salvar os dados em um arquivo json, valindando se o modo de abertura não é binário (b), pois 
            é incompatível com strings → json.dump() espera texto ou se é uma operação de leitura/escrita (+) que pode corromper o 
            arquivo 
            """

            if file_mode.is_binary() or file_mode.is_read_write():
                raise ValueError(f"Modo '{file_mode.value}' não é permitido para exportação de JSON.")
            
            else:
                
                with open(file_path, mode=file_mode.value, encoding=encoding.value) as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                
                print(f'Arquivo salvo com sucesso em: {file_path}')


class DataFrameToJsonFile(DataFrameToExporter):
    """
    Classe responsável por implementar DataFrameToFileTemplate para conversão de dataframes pandas para json-like
    """

    def __init__(self):
        super().__init__(
            converter=JsonConverter(),
            saver=JsonSaver()
        )
    


    