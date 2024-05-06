from lxml import etree

def xmlToString(xmlRoot):
    tree = etree.parse(xmlRoot)
    return str(etree.tostring(tree, encoding='utf8', method='xml'))[2:-1]