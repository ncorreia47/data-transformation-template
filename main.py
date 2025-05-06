import pandas as pd
from dataframe_to_json import DataFrameToJsonFile

# Exemplo de DataFrame
df = pd.DataFrame({
    'nome': ['Ana', 'Bruno'],
    'idade': [28, 34],
    'cidade': ['Curitiba', 'São Paulo'],
    'estado': ['PR', 'SP'],
    'idade' : [25,32]
})

DataFrameToJsonFile().export(df=df, file_name='output.json', path_file=None)