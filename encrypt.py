# Pedir al usuario la ruta de la imagen y el tamaño de la llave a utilizar
imagen = input("Ingrese direccion de la imagen: ")
llave = input("Ingrese tamaño de llave (0-256): ")

# Abrir la imagen y guardar su contenido en una variable
archivo_imagen = open(imagen, 'rb')

# Leer el contenido de la imagen en un byte array (arreglo de la información individual de cada byte de la imagen)
data_imagen = archivo_imagen.read()
data_imagen = bytearray(data_imagen)

# Recorrer el arreglo y encriptar cada uno de los bytes con la llave dada (elevando su contenido a la potencia de la llave (XOR))
for i, valor in enumerate(data_imagen):
  data_imagen[i] = valor ^ int(llave)

# Abrir y escribir el archivo de salida (misma imagen) y escribir el contenido modificado previamente 
archivo_salida = open(imagen, 'wb')
archivo_salida.write(data_imagen)

# Cerrar ambos archivos (entrada y salida)
archivo_imagen.close()
archivo_salida.close()