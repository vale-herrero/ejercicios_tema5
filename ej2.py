import sys

try:
    archivo = open('contador.txt', 'r+')
    contador =  int(archivo.read()) 
    archivo.seek(0)
    archivo.truncate()
except OSError:
    print('Archivo no existe! se creará con el valor de 0 visitas')
    archivo = open('contador.txt', 'w+')
    contador = 0
    print('Archivo creado!!')
try:
    comando = sys.argv[1]    
    if comando == 'inc':
	    contador = contador + 1
        print('Incrementando el número de visitas debido al argumento inc')
        print('Nuevo valor: {}'.format(contador))
    elif comando == 'dec':
	    print('Decrementando el número de visitas debido al argumento dec')
	    contador = contador - 1
	    print('Nuevo valor: {}'.format(contador))
	    
    else:
	    print('Número de visitas leído del archivo contador: {}'.format(contador))  
    print('Almacenando nuevo valor')
    archivo.write(str(contador)) 

except:
    print('Número de visitas leído del archivo contador: {}'.format(contador))
    if contador == 0:
        archivo.write(str(contador))

archivo.close()