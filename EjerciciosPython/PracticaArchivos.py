import csv
from datetime import datetime

archivo_personas = 'personas.txt'
archivo_plantilla = 'carta_Solicitud.txt'

class OficinaGenerator:
    def __init__(self, archivo_personas, archivo_plantilla):
        self.archivo_personas = archivo_personas
        self.archivo_plantilla = archivo_plantilla
        self.personas = []
        self.plantilla = ""

    def leer_personas(self):
        try:
            with open(self.archivo_personas, mode='r', encoding='utf-8') as file:
                lector = csv.DictReader(file)
                for fila in lector:
                    if 'fechaNacimiento' in fila:  # Validar campo requerido
                        fecha_nacimiento = datetime.strptime(fila['fechaNacimiento'], '%Y-%m-%d')
                        fila['edad'] = (datetime.now() - fecha_nacimiento).days // 365
                        self.personas.append(fila)
                    else:
                        print(f"Advertencia: 'fechaNacimiento' no encontrado en la fila {fila}.")
        except FileNotFoundError:
            print(f"Error: El archivo {self.archivo_personas} no fue encontrado.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def leer_plantilla(self):
        try:
            with open(self.archivo_plantilla, mode='r', encoding='utf-8') as file:
                self.plantilla = file.read()
        except FileNotFoundError:
            print(f"Error: El archivo {self.archivo_plantilla} no fue encontrado.")
        except Exception as e:
            print(f"Error al leer la plantilla: {e}")

    def generar_oficio(self, persona):
        return self.plantilla.format(**persona)

    def guardar_oficio(self, oficio, persona):
        nombre_archivo = f"oficio_{persona['nombre']}_{persona['apellido1']}.txt"
        try:
            with open(nombre_archivo, mode='w', encoding='utf-8') as file:
                file.write(oficio)
            print(f"Oficio generado: {nombre_archivo}")
        except Exception as e:
            print(f"Error al guardar el oficio: {e}")

    def ejecutar(self):
        self.leer_personas()
        self.leer_plantilla()
        for persona in self.personas:
            oficio = self.generar_oficio(persona)
            self.guardar_oficio(oficio, persona)

generador = OficinaGenerator(archivo_personas, archivo_plantilla)
generador.ejecutar()