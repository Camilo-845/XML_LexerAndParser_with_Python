from enum import Enum
class tokenType (Enum):
    APERTURA_DE_ETIQUETA = 0
    NOMBRE_DE_ETIQUETA = 1
    CIERRE_DE_ETIQUETA = 2
    APERTURA_DE_ETIQUETA_DE_CIERRE = 3
    CIERRE_ESPECIAL_DE_ETIQUETA = 4
    CADENA = 5
    ASIGNACION = 6
    CADENA_DE_TEXTO_TIPO_STRING = 7

class Token:
    def __init__(self, token_type:tokenType, lexema: str, line = int) -> None:
        self.token_type = token_type
        self.lexema = lexema
        self.line = line
    def __str__(self) -> str:
        return f'{self.token_type}({self.lexema}) - line({self.line})'