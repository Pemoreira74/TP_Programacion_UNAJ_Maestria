# rutina para crear datos falsos
from faker import Faker
import random

# Cantidad de lineas a generar
cantidad = 100

# Configurar Faker para nombres en español
fake = Faker('es_ES')

# Generar datos y escribir en el archivo CSV
# queda en la carpeta datos (debe estar creada...)
with open('datos/estudiantes.csv', 'w', encoding='utf-8') as file:
    for _ in range(100):
        nombre = fake.first_name()
        apellido = fake.last_name()
        nota_mat = round(random.uniform(0, 10), 2)
        nota_fis = round(random.uniform(0, 10), 2)
        nota_lit = round(random.uniform(0, 10), 2)
        
        # Escribir la línea sin cabeceras y con comas como separadores
        file.write(f"{nombre},{apellido},{nota_mat:.2f},{nota_fis:.2f},{nota_lit:.2f}\n")

print("Archivo 'estudiantes.csv' generado exitosamente con 100 registros.")