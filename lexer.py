from Token import Token, tokenType
import re

class lexer:
    def __init__(self, text:str) -> None:
        self.textIter = iter(text)
        self.code = text
        self.current = None
        self.currentLine = 1
    def continuar (self):
        try:
            self.current = next(self.textIter)
        except StopIteration:
            self.current = None

    def scan(self):
        while self.current is not None:
            if(self.current == '\n'):
                self.currentLine += 1
                self.continuar()
            if(self.current in ('\t',' ')):
                self.continuar()
            elif (self.current == "="):
                self.continuar()
                return Token(tokenType.ASIGNACION,"=",self.currentLine)
            elif (self.current == "\""):
                response:Token = self.evaluarCadena(tokenType.CADENA_DE_TEXTO_TIPO_STRING, "[^<,>]")
                if(response != None and not re.search("\"[^<,>]*\"", response.lexema)):
                    return None
                return response
            elif (self.current == '<'):
                response =  [self.evaluarTipoComplejo(['<','</'],[tokenType.APERTURA_DE_ETIQUETA,tokenType.APERTURA_DE_ETIQUETA_DE_CIERRE],"[<,/]")]
                if(response != None):
                    response.append(self.evaluarCadena(tokenType.NOMBRE_DE_ETIQUETA,"[a-z,A-Z,0-9,_,:]"))
                return response
            elif (self.current == '/'):
                return self.evaluarTipoComplejo(['/>'],[tokenType.CIERRE_ESPECIAL_DE_ETIQUETA],"[>,/]")
            elif (self.current == '>'):
                return self.evaluarTipoComplejo(['>'],[tokenType.CIERRE_DE_ETIQUETA],">")
            elif (re.search("[^<,>]",self.current)):
                return self.evaluarCadena(tokenType.CADENA,"[^<,>,\",=]")
            else:
                self.continuar()
        return None

    def scanAll (self):
        self.continuar()
        tokens = []
        while True:
            token = self.scan()
            if(type(token) == list):
                for tokenItem in token:
                    if tokenItem is None:
                        if self.current != None:
                            print("Error de lexico en la linea: ", self.currentLine)
                        break
                    tokens.append(tokenItem)
            else:
                if token is None:
                    if self.current != None:
                        print("Error de lexico en la linea: ", self.currentLine)
                    break
                tokens.append(token)
        return tokens
    
    def evaluarTipoComplejo(self, cadenas:list, tipos:list, regex:str):
        cadena:str = ''
        logitudMaxima = len(max(cadenas))
        while self.current != None and logitudMaxima > len(cadena) and re.search(regex,self.current):
            cadena += self.current
            self.continuar()
        if cadena in cadenas:
            index = cadenas.index(cadena)
            return Token(tipos[index], cadena, self.currentLine)
        return None

    def evaluarCadena(self,tipo,regex):
        cadena:str = ''
        while self.current != None and re.search(regex,self.current):
            cadena += self.current
            self.continuar()
        if(cadena != ''):
            return Token(tipo, cadena, self.currentLine)
        return None
lexer1 = lexer("<xsd:element name=342>\n<xsd:complexType>\n<xsd:element name = \"addresasdfasds\">\n<xsd:element name=\"shipTo\"/>\n</xsd:element name=\"address\">\n</xsd:complexType>\n</xsd:element name=\"asdfas\">").scanAll()
for i in lexer1:
    print(str(i))