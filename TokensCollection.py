from collections import deque
from Token import tokenType

class TokenCollection:
    def __init__(self, collection:list) -> None:
        self.collectionIter = iter(collection)
        self.currentCollection:list = None
        self.pilaDeEtiquetas = deque()

    def __continuar__ (self):
        try:
            self.currentCollection = next(self.collectionIter)
        except StopIteration:
            self.currentCollection = None

    def anidarEtiquetas(self):
        self.__continuar__()
        while True:
            if(self.currentCollection is None):
                if(len(self.pilaDeEtiquetas)>0):
                    print("Error de lexico (Anidamiento de etiquetas erroneo)")
                break
            if(self.currentCollection[0].token_type == tokenType.CADENA):
                self.pilaDeEtiquetas.append(self.currentCollection)
            elif(self.currentCollection[0].token_type == tokenType.APERTURA_DE_ETIQUETA):
                self.pilaDeEtiquetas.append(self.currentCollection)
            elif(self.currentCollection[0].token_type == tokenType.APERTURA_DE_ETIQUETA_DE_CIERRE):
                anidamientoRecursivo = self.__anidarEtiquetas__(self.currentCollection)
                if(anidamientoRecursivo is None):
                    break
            self.__continuar__()

        """ pila = deque()
        anidamientos = []
        pila.append(self.tokensCollection[0])
        for collection in range(1, len(self.tokensCollection)-1):
            if(collection[0].token_type == tokenType.CADENA):
                pila.append(collection)
            elif(collection[0].token_type == tokenType.APERTURA_DE_ETIQUETA):
                pila.append(collection)
            elif(collection[0].token_type == tokenType.APERTURA_DE_ETIQUETA_DE_CIERRE):
                anidamientos.append(self.__anidarEtiquetas__(pila, collection))
                return """
                
    def __anidarEtiquetas__(self, collection):
        
        anidamiento = []
        while True:
            if (self.__evaluarCollecionEtiquetas__(self.pilaDeEtiquetas.pop(),collection)):
                anidamiento.append(self.currentCollection)
                anidamiento.append(anidamiento)
                anidamiento.append(collection)
                return True
            if(len(self.pilaDeEtiquetas)<=0):
                print("Error de lexico (Anidamiento de etiquetas erroneo), etiqueta: ", collection[1], " nunca se abre:")
                return None
        """ anidamientos = []
        anidamiento = []
        currentCollection:list = pila.pop()
        while True:
            if (self.__evaluarCollecionEtiquetas__(currentCollection,collection)):
                anidamientos.append(currentCollection)
                anidamientos.append(anidamiento)
                anidamientos.append(collection)
                break; 
            if(len(pila) == 0):
                print("Error de lexico, hay un anidamiento de eqtiquetas no valido")
                return None
            anidamiento.append(currentCollection)
            currentCollection = pila.pop() """

    def __evaluarCollecionEtiquetas__(self, clltn1:list, clltn2:list):
        return clltn1[1].lexema == clltn2[1].lexema