class ClienteInvalidoError(Exception):
    """Error cuando los datos del cliente son inválidos"""
    pass


class ServicioNoDisponibleError(Exception):
    """Error cuando el servicio no está disponible"""
    pass


class ReservaError(Exception):
    """Error general relacionado con reservas"""
    pass


class DuracionInvalidaError(Exception):
    """Error cuando la duración ingresada no es válida"""
    pass