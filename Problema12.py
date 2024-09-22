




extensiones = ['.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip']
MIMES = ['image/gif', 'image/jpeg', 'image/jpeg', 'image/png', 'application/pdf', 'text/plain', 'application/zip']


nombre = input("Ingrese el nombre del archivo: ")

if '.' in nombre:
    extension = '.' + nombre.split('.')[-1].lower()
else:
    extension = ''

if extension in extensiones:
    tipoMIME = MIMES[extensiones.index(extension)]
else:
    tipoMIME = 'application/octet-stream'

print(tipoMIME)
