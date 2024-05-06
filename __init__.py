from xmlToString import xmlToString
from Parser import Parser

xmlString = xmlToString("./Estructura.xml")
parser = Parser(xmlString)

collecciones = parser.analizarSintaxis()
index = 1
for collleccion in collecciones:
    print(f"Colleccion {index}:")
    for token in collleccion:
        print(token)
    index += 1