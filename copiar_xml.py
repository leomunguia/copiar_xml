import os
import shutil

# Ruta de los directorios
directorio_origen = '//sia/AEGF/DGAGFD/VMCR/PFEF/CP2023/1_XML/001/001.1.1/11_XML/CFDI 2023'
directorio_destino = 'G:/Mi unidad/ASF/CP 2023/XMLs/AGS/SEFI/xml'


def copiar_archivos_xml(directorio_origen, directorio_destino):
    # Recorrmos todos los directorios y subdirectorios
    for root, dirs, files in os.walk(directorio_origen):
        for file in files:
            # Verificamos si el archivo es un XML
            if file.endswith('.xml'):
                # Construimos la ruta completa del archivo fuente
                archivo_origen = os.path.join(root, file)
                # Construimos la ruta completa de destino
                archivo_destino = os.path.join(directorio_destino, file)
                
                # Si el archivo ya existe en el destino, lo sobrescribimos
                shutil.copy2(archivo_origen, archivo_destino)
                print(f'Archivo copiado: {archivo_origen} -> {archivo_destino}')



# Invocamos la función
copiar_archivos_xml(directorio_origen, directorio_destino)
