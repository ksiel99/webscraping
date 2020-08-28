from urllib.request import urlopen
#pagina = urlopen("https://w3schools.com/")
print(pagina.read())
print('PAGINA:', pagina)
print('URL:', pagina.geturl())

headers = pagina.info()
print('FECHA :', headers['date'])
print('HEADERS:,')
print('------------------------')
print(headers)

data = pagina.read().decode('utf-8')
print('LENGTH:', len(data))
print('DATA :')
print('------------------------')
print(data)