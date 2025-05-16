from enum import Enum, unique


@unique
class FileMode(str, Enum):
    """
    Enum com métodos de abertura de arquivos:
    READ = 'r', WRITE = 'w', APPEND = 'a', EXCLUSIVE = 'x', READ_WRITE = 'r+', WRITE_READ = 'w+', APPEND_READ = 'a+'
    """

    READ = 'r'
    WRITE = 'w'
    APPEND = 'a'
    EXCLUSIVE = 'x'
    READ_WRITE = 'r+'
    WRITE_READ = 'w+'
    APPEND_READ = 'a+'


    def is_binary(self) -> bool:
        return 'b' in self.value


    def is_read_write(self) -> bool:
        return '+' in self.value


@unique
class FileEncoding(str, Enum):
    """
    Enum com métodos de encodings mais utilizados
    """

    UTF8 = 'utf-8'
    UTF8_SIG = 'utf-8-sig'         # Com BOM
    LATIN1 = 'latin-1'             # ISO-8859-1
    ASCII = 'ascii'
    UTF16 = 'utf-16'
    UTF32 = 'utf-32'
    CP1252 = 'cp1252'              # Windows-1252