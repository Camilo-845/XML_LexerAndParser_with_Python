from lexer import Lexer
from Token import tokenType
from Token import Token
from TokensCollection import TokenCollection

elementosSintacticos = [
    [tokenType.APERTURA_DE_ETIQUETA, tokenType.NOMBRE_DE_ETIQUETA, tokenType.CIERRE_DE_ETIQUETA]
]

class Parser: 
    def __init__(self, text:str):
        self.tokensIter = iter(Lexer(text).scanAll())
        self.currentToken:Token = None
        self.tokensCollection:TokenCollection = None
    
    def __continuar__ (self):
        try:
            self.currentToken = next(self.tokensIter)
        except StopIteration:
            self.currentToken = None
       
    def __scan__(self):
         while self.currentToken is not None:
            tokensCollection = []
            if(self.currentToken.token_type is not None and self.currentToken.token_type in (tokenType.APERTURA_DE_ETIQUETA, tokenType.APERTURA_DE_ETIQUETA_DE_CIERRE)):
                tokensCollection.append(self.currentToken)
                self.__continuar__()
                if(self.currentToken.token_type is not None and self.currentToken.token_type == tokenType.NOMBRE_DE_ETIQUETA):
                    tokensCollection.append(self.currentToken)
                    self.__continuar__()
                    if(self.currentToken.token_type is not None and self.currentToken.token_type in (tokenType.CIERRE_DE_ETIQUETA, tokenType.CIERRE_ESPECIAL_DE_ETIQUETA)):
                        tokensCollection.append(self.currentToken)
                        self.__continuar__()
                        return tokensCollection
                    elif(self.currentToken.token_type is not None and self.currentToken.token_type == tokenType.CADENA):
                        while True:
                            if(self.currentToken.token_type is not None and self.currentToken.token_type == tokenType.CADENA):
                                tokensCollection.append(self.currentToken)
                                self.__continuar__()
                                if(self.currentToken.token_type is not None and self.currentToken.token_type == tokenType.ASIGNACION):
                                    tokensCollection.append(self.currentToken)
                                    self.__continuar__()
                                    if(self.currentToken.token_type is not None and self.currentToken.token_type == tokenType.CADENA_DE_TEXTO_TIPO_STRING):
                                        tokensCollection.append(self.currentToken)
                                        self.__continuar__()
                                    else:
                                        return None
                                else:
                                    return None
                            elif(self.currentToken.token_type is not None and self.currentToken.token_type == tokenType.CIERRE_DE_ETIQUETA):
                                tokensCollection.append(self.currentToken)
                                self.__continuar__()
                                return tokensCollection
                            elif(self.currentToken.token_type is not None and self.currentToken.token_type == tokenType.CIERRE_ESPECIAL_DE_ETIQUETA):
                                if(tokensCollection[0].token_type == tokenType.APERTURA_DE_ETIQUETA_DE_CIERRE):
                                    return None
                                tokensCollection.append(self.currentToken)
                                self.__continuar__()
                                return tokensCollection
                            else:
                                return None
                    else:
                        return None
                else:
                    return None
            elif(self.currentToken.token_type is not None and self.currentToken.token_type == tokenType.CADENA):
                return [self.currentToken]
            else:
                return None

    def __scanAll__(self):
        conjuntos = []
        self.__continuar__()
        while True:
            conjuntoTokens = self.__scan__()
            if(conjuntoTokens is None or len(conjuntoTokens) <= 0):
                if(self.currentToken != None):
                    print("Error de lexico cerca de la linea: ", self.currentToken.line)
                break
            conjuntos.append(conjuntoTokens)
        self.tokensCollection = conjuntos
        return conjuntos  

    def analizarSintaxis (self) :
        scaneo = self.__scanAll__()
        collection = TokenCollection(scaneo)
        collection.anidarEtiquetas()
        return scaneo
    