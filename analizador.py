# lectura de librerias y modulos necesarios
import pandas as pd
from typing import List, Dict
from estudiante import Estudiante


class AnalizadorNota:
    # Metodo constructor
    def __init__(self, ruta_csv: str) -> None:
        # Vamos a proteger la lectura del archivo
        try:
            self.df = pd.read_csv(ruta_csv)
            self.estudiantes = self._crear_estudiantes()
        # Si hay un error de lectura del archivo porque no existe
        except FileNotFoundError:
            raise FileNotFoundError(f"El archivo {ruta_csv} no fue encontrado")
        # Si se produce cualquier otro error
        except Exception as e:
            raise Exception(f"Error al leer el archivo CSV: {str(e)}")

    # Metodo crear lista de estudiantes (metodo privado, no expuesto)
    def _crear_estudiantes(self) -> List[Estudiante]:
        """
        Crea una lista de objetos Estudiante a partir del DataFrame
        """
        return [
            Estudiante(
                row["nombre"],
                row["apellido"],
                row["matematicas"],
                row["fisica"],
                row["literatura"],
            )
            for _, row in self.df.iterrows()
        ]

    # Metodos publicos
    def calcular_promedios_asignaturas(self) -> Dict[str, float]:
        """
        Calcula el promedio por asignatura
        """
        return {
            # conversion a texto porque son floats de numpy
            "Matemáticas": float(f"{self.df['matematicas'].mean():.2f}"),
            "Física": float(f"{self.df['fisica'].mean():.2f}"),
            "Literatura": float(f"{self.df['literatura'].mean():.2f}"),
        }

    def porcentaje_aprobacion(self) -> float:
        """
        Calcula el porcentaje de estudiantes aprobados
        """
        aprobados = sum(
            1 for e in self.estudiantes if e.obtener_sit() == "Aprobado"
        )
        return round((aprobados / len(self.estudiantes)) * 100, 2)

    def asignatura_max_min_rendimiento(self) -> Dict[str, str]:
        """
        Identifica la asignatura con mayor y menor rendimiento
        """
        promedios = self.calcular_promedios_asignaturas()
        max_asig = max(promedios.items(), key=lambda x: x[1])
        min_asig = min(promedios.items(), key=lambda x: x[1])
        return {
            "mayor_rendimiento": f"{max_asig[0]} ({max_asig[1]})",
            "menor_rendimiento": f"{min_asig[0]} ({min_asig[1]})",
        }

    def generar_informe(self) -> pd.DataFrame:
        """
        Genera un DataFrame con toda la información procesada
        """
        data = []
        for est in self.estudiantes:
            data.append(
                {
                    "Estudiante": f"{est.nombre} {est.apellido}",
                    "Promedio": est.calcular_prom(),
                    "Situación": est.obtener_sit(),
                    "Matemáticas": est.nota_mat,
                    "Física": est.nota_fis,
                    "Literatura": est.nota_lit,
                }
            )
        return pd.DataFrame(data)
