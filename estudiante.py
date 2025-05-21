# Clase Estudiante
class Estudiante:
    # Metodo constructor
    def __init__(
        self,
        nombre: str,
        apellido: str,
        nota_mat: float,
        nota_fis: float,
        nota_lit: float,
    ):
        self.nombre = self._validar_nombre(nombre)
        self.apellido = self._validar_nombre(apellido)
        self.nota_mat = self._validar_nota(nota_mat)
        self.nota_fis = self._validar_nota(nota_fis)
        self.nota_lit = self._validar_nota(nota_lit)

    # Se usdecora con metodo estatico para que sea una funcion simple sin recurrir al self
    @staticmethod
    def _validar_nombre(dato: str) -> str:
        """
        Valida que el nombre o apellido sea un string no vacío
        """
        if not isinstance(dato, str):
            raise TypeError("El nombre/apellido debe ser una cadena de texto")
        if not dato.strip():
            raise ValueError("El nombre/apellido no puede estar vacío")
        if any(char.isdigit() for char in dato):
            raise ValueError("El nombre/apellido no puede contener números")
        return dato.strip()

    # Se decora con metodo estatico para que sea una funcion simple sin recurrir al self
    @staticmethod
    def _validar_nota(dato: float) -> float:
        """
        Valida que la nota sea un número entre 0 y 10
        """
        try:
            nota = float(dato)
        except (ValueError, TypeError):
            raise ValueError("La nota debe ser un valor numérico")

        if not 0 <= nota <= 10:
            raise ValueError("La nota debe estar entre 0 y 10")
        return round(nota, 2)

    # Metodos de la clase
    def calcular_prom(self) -> float:
        """
        Calcula el promedio de las tres asignaturas
        """
        return round((self.nota_mat + self.nota_fis + self.nota_lit) / 3, 2)

    def obtener_sit(self) -> str:
        """
        Determina si el estudiante está aprobado (nota >= 6)
        """
        return "Aprobado" if self.calcular_prom() >= 6 else "Reprobado"

    def __str__(self):
        """
        Se redefine el dunder para que el print de Estudante reporte sus atributos
        """
        return f"{self.nombre} {self.apellido} - Promedio: {self.calcular_prom()} - {self.obtener_sit()}"
