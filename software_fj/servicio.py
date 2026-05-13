from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponibleError


class Servicio(ABC):

    def __init__(self, nombre, tarifa_base):

        if tarifa_base <= 0:
            raise ServicioNoDisponibleError(
                "La tarifa del servicio debe ser mayor a cero"
            )

        self.nombre = nombre
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def __init__(self):
        super().__init__("Reserva de Sala", 50000)

    def calcular_costo(self, duracion):
        return self.tarifa_base * duracion

    def descripcion(self):
        return "Servicio de reserva de salas empresariales"


class AlquilerEquipo(Servicio):

    def __init__(self):
        super().__init__("Alquiler de Equipos", 30000)

    def calcular_costo(self, duracion):
        return (self.tarifa_base * duracion) + 10000

    def descripcion(self):
        return "Servicio de alquiler de equipos tecnológicos"


class AsesoriaEspecializada(Servicio):

    def __init__(self):
        super().__init__("Asesoría Especializada", 80000)

    def calcular_costo(self, duracion):
        descuento = 0

        if duracion >= 5:
            descuento = 0.10

        total = self.tarifa_base * duracion
        return total - (total * descuento)

    def descripcion(self):
        return "Servicio de asesorías especializadas"