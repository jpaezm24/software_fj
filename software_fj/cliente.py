from excepciones import ClienteInvalidoError


class Cliente:

    def __init__(self, nombre, documento, telefono):

        if not nombre.strip():
            raise ClienteInvalidoError("El nombre no puede estar vacío")

        if not str(documento).isdigit():
            raise ClienteInvalidoError("El documento debe contener solo números")

        if not str(telefono).isdigit():
            raise ClienteInvalidoError("El teléfono debe contener solo números")

        self.__nombre = nombre
        self.__documento = documento
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre

    def get_documento(self):
        return self.__documento

    def get_telefono(self):
        return self.__telefono

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - Documento: {self.__documento}"