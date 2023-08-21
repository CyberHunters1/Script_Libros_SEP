import os
import requests
import threading

# Función para descargar una imagen desde una URL
def descargar_imagen(url, nombre_archivo):
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            with open(nombre_archivo, 'wb') as archivo:
                archivo.write(respuesta.content)
            print("Imagen descargada exitosamente como", nombre_archivo)
            return True
        else:
            print("Error al descargar la imagen. Código de estado:", respuesta.status_code)
    except Exception as e:
        print("Ocurrió un error:", e)
    return False

# Función para realizar la descarga en un hilo
def descargar_en_hilo(url, nombre_archivo):
    if os.path.exists(nombre_archivo):
        print("El archivo ya existe:", nombre_archivo)
    else:
        print("Intentando descargar:", url)
        descargar_imagen(url, nombre_archivo)

# Lista de URLs de libros
urls_libros = [
    # Lista de enlaces a los libros
   "https://www.conaliteg.sep.gob.mx/2023/c/P1LPM/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1SDA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1TPA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P2PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P2PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P2PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P2SDA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P2MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3LPM/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3SDA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P4MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P4PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P4PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P4PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P4SDA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P0CMA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P0SHA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5LPM/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5SDA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P6MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P6PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P6PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P6PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P6SDA/"
]

extension = ".jpg"

# Iterar a través de cada enlace de libro
for base_url in urls_libros:
    # Extraer el nombre del libro del enlace
    nombre_libro = base_url.split("/")[-2]

    # Crear una carpeta para el libro si no existe
    carpeta_libro = f"{nombre_libro}/"
    if not os.path.exists(carpeta_libro):
        os.makedirs(carpeta_libro)
        
    threads = []
    contador = 0
     while True:
        numero_imagen = str(contador).zfill(3)
        url_imagen = f"{base_url}{numero_imagen}{extension}"
        nombre_archivo = f"{carpeta_libro}imagen_descargada_{contador}.jpg"

        # Crear un hilo para la descarga
        thread = threading.Thread(target=descargar_en_hilo, args=(url_imagen, nombre_archivo))
        thread.start()
        threads.append(thread)

        contador += 1

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()
