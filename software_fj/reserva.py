from excepciones import ReservaError, DuracionInvalidaError


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise DuracionInvalidaError(
                "La duración debe ser mayor a cero"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        if self.estado == "Confirmada":
            raise ReservaError("La reserva ya estaba confirmada")

        self.estado = "Confirmada"

    def cancelar(self):

        if self.estado == "Cancelada":
            raise ReservaError("La reserva ya estaba cancelada")

        self.estado = "Cancelada"

    def procesar_reserva(self):

        costo = self.servicio.calcular_costo(self.duracion)

        return {
            "cliente": self.cliente.get_nombre(),
            "servicio": self.servicio.nombre,
            "duracion": self.duracion,
            "estado": self.estado,
            "costo": costo
        }