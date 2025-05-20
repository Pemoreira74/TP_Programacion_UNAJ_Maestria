# lectura de librerias y modulos necesarios
from analizador import AnalizadorNota


def main():
    # Configuración inicial
    ruta_csv = "../datos/estudiantes.csv"

    # Procesamiento de datos
    analizador = AnalizadorAcademico(ruta_csv)
    informe = analizador.generar_informe()

    # Resultados
    print("\n=== INFORME INDIVIDUAL ===")
    print(informe.to_string(index=False))

    print("\n=== ESTADÍSTICAS GENERALES ===")
    print(f"Promedios por asignatura: {analizador.calcular_promedios_asignaturas()}")
    print(f"Porcentaje de aprobación: {analizador.porcentaje_aprobacion()}%")
    print(f"Rendimiento por asignatura: {analizador.asignatura_max_min_rendimiento()}")


if __name__ == "__main__":
    main()
