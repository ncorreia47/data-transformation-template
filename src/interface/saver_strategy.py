from abc import ABC, abstractmethod
from utils.enums import FileMode, FileEncoding


class Saver(ABC):
    """
    Classe responsável por implementar os métodos de salvamento de arquivos
    """

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
