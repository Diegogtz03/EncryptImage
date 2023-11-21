# Función para validar que la ruta de la imagen ingresada por el usuario sea correcta
def validateImage(image):
  # Lista de extensiones de imagen válidas
  image_extensions = [".jpg", ".JPG", ".jpeg", ".JPEG", ".png", ".PNG", ".gif", ".GIF"]
  flag = False

  # Revisar si la ruta de la imagen termina con alguna de las extensiones válidas
  for extension in image_extensions:
    if image.endswith(extension):
      flag = True
      break

  # Si no termina con ninguna de las extensiones válidas, entonces no es una imagen válida
  if not flag:
    print("No es una imagen valida")
    return False
  
  # Si pasa el primer filtro, intentar abrir el archivo de la imagen
  try:
    archivo_imagen = open(image, 'rb')
    archivo_imagen.close()
    return True
  except:
    # Si no se puede abrir, entonces no es una imagen válida
    print("No es una imagen valida")
    return False

# Función que valida que la llave ingresada sea correcta (0-256)
def validateKey(key):
  # Verificar que la llave sea un número entero y no caracteres o vacío
  if not key.isnumeric() or key == "":
    print("La llave debe ser un número entero")
    return False
  
  # Verificar que la llave esté dentro del rango permitido de la llave (0-256)
  if int(key) < 0 or int(key) > 256:
    print("La llave debe ser un número entre 0 y 256")
    return False
  else:
    return True


# Pedir al usuario la ruta de la imagen y el tamaño de la llave a utilizar para desencriptar, y validar que sean correctos
imagen = input("Ingrese direccion de la imagen: ")

while (not validateImage(imagen)):
  imagen = input("Ingrese direccion de la imagen: ")

llave = input("Ingrese tamaño de llave (0-256): ")

while (not validateKey(llave)):
  llave = input("Ingrese tamaño de llave (0-256): ")

# Abrir la imagen encriptada y guardar su contenido en una variable
archivo_imagen = open(imagen, 'rb')

# Leer el contenido de la imagen en un byte array (arreglo de la información individual de cada byte de la imagen)
data_imagen = archivo_imagen.read()
data_imagen = bytearray(data_imagen)

# Recorrer el arreglo y desencriptar cada uno de los bytes con la llave dada 
# (elevando el contenido de cada byte a la potencia de la llave dada)
for i, valor in enumerate(data_imagen):
  data_imagen[i] = valor ^ int(llave)

# Abrir y escribir el archivo de salida (misma imagen) y escribir el contenido modificado previamente 
archivo_salida = open(imagen, 'wb')
archivo_salida.write(data_imagen)

# Cerrar ambos archivos (entrada y salida)
archivo_imagen.close()
archivo_salida.close()