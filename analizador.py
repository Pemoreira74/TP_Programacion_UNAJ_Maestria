# lectura de librerias y modulos necesarios
import pandas as pd
from typing import List, Dict
from estudiante import Estudiante


class AnalizadorNota:
    def __init__(self, ruta_csv: str):
        self.df = pd.read_csv(ruta_csv)
        self.estudiantes = self._crear_estudiantes()

    def _crear_estudiantes(self) -> List[Estudiante]:
        """
        Crea objetos Estudiante a partir del DataFrame
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

    def calcular_promedios_asignaturas(self) -> Dict[str, float]:
        """
        Calcula el promedio por asignatura
        """
        return {
            "Matemáticas": round(self.df["matematicas"].mean(), 2),
            "Física": round(self.df["fisica"].mean(), 2),
            "Literatura": round(self.df["literatura"].mean(), 2),
        }

    def porcentaje_aprobacion(self) -> float:
        """
        Calcula el porcentaje de estudiantes aprobados
        """
        aprobados = sum(
            1 for e in self.estudiantes if e.situacion_academica() == "Aprobado"
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
                    "Promedio": est.calcular_promedio(),
                    "Situación": est.situacion_academica(),
                    "Matemáticas": est.nota_mat,
                    "Física": est.nota_fis,
                    "Literatura": est.nota_lit,
                }
            )
        return pd.DataFrame(data)
