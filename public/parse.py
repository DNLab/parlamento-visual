from lxml import etree

parser = etree.XMLParser()

f = open('mapa.html', 'rb')
mapa = f.read()
f.close

tree = etree.XML(mapa, parser)
 
[a.attrib['coords'] for a in tree.findall('area')]

for a in tree.findall('area'):
    nombre = a.attrib['title'].split(',')[1].strip() + ' ' + a.attrib['title'].split(',')[0]
    id = a.attrib['id'].replace('cp', '') 
    x = a.attrib['coords'].split(',')[0]
    y = a.attrib['coords'].split(',')[1]
    print ','.join((id,nombre,x,y))

