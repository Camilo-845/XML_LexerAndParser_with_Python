from Parser import Parser

xmlFilePath = "./Estructura.xml"

f = open(xmlFilePath, 'r')
Datos = f.read()
f.close()


parser = Parser(Datos)


collecciones = parser.analizarSintaxis()
index = 1
for collleccion in collecciones:
    print(f"Colleccion {index}:")
    for token in collleccion:
        print(token)
    index += 1