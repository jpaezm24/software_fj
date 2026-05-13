from cliente import Cliente
from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from reserva import Reserva

from excepciones import (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaError,
    DuracionInvalidaError
)


def registrar_log(mensaje):

    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")


def main():

    print("=" * 50)
    print("SISTEMA SOFTWARE FJ")
    print("=" * 50)

    operaciones = 0

    # OPERACIÓN 1
    try:
        cliente1 = Cliente(
            "Javier",
            "123456",
            "3001234567"
        )

        print(cliente1.mostrar_info())

        registrar_log(
            "[INFO] Cliente válido registrado"
        )

        operaciones += 1

    except ClienteInvalidoError as e:

        print(e)

        registrar_log(
            f"[ERROR] {e}"
        )

    # OPERACIÓN 2
    try:

        cliente2 = Cliente(
            "",
            "abc",
            "telefono"
        )

        operaciones += 1

    except ClienteInvalidoError as e:

        print(f"Error cliente: {e}")

        registrar_log(
            f"[ERROR] {e}"
        )

    # OPERACIÓN 3
    try:

        servicio1 = ReservaSala()

        print(servicio1.descripcion())

        registrar_log(
            "[INFO] Servicio ReservaSala creado"
        )

        operaciones += 1

    except ServicioNoDisponibleError as e:

        print(e)

        registrar_log(
            f"[ERROR] {e}"
        )

    # OPERACIÓN 4
    try:

        servicio2 = AlquilerEquipo()

        print(servicio2.descripcion())

        registrar_log(
            "[INFO] Servicio AlquilerEquipo creado"
        )

        operaciones += 1

    except ServicioNoDisponibleError as e:

        print(e)

        registrar_log(
            f"[ERROR] {e}"
        )

    # OPERACIÓN 5
    try:

        servicio3 = AsesoriaEspecializada()

        print(servicio3.descripcion())

        registrar_log(
            "[INFO] Servicio AsesoriaEspecializada creada"
        )

        operaciones += 1

    except ServicioNoDisponibleError as e:

        print(e)

        registrar_log(
            f"[ERROR] {e}"
        )

    # OPERACIÓN 6
    try:

        reserva1 = Reserva(
            cliente1,
            servicio1,
            2
        )

        reserva1.confirmar()

        datos = reserva1.procesar_reserva()

        print(datos)

        registrar_log(
            "[INFO] Reserva confirmada correctamente"
        )

        operaciones += 1

    except (
        ReservaError,
        DuracionInvalidaError
    ) as e:

        print(e)

        registrar_log(
            f"[ERROR] {e}"
        )

    # OPERACIÓN 7
    try:

        reserva2 = Reserva(
            cliente1,
            servicio2,
            -3
        )

        operaciones += 1

    except DuracionInvalidaError as e:

        print(f"Error duración: {e}")

        registrar_log(
            f"[ERROR] {e}"
        )

    # OPERACIÓN 8
    try:

        reserva3 = Reserva(
            cliente1,
            servicio3,
            6
        )

        reserva3.confirmar()

        datos = reserva3.procesar_reserva()

        print(datos)

        registrar_log(
            "[INFO] Reserva asesoría creada"
        )

        operaciones += 1

    except Exception as e:

        print(e)

        registrar_log(
            f"[ERROR] {e}"
        )

    # OPERACIÓN 9
    try:

        reserva1.confirmar()

        operaciones += 1

    except ReservaError as e:

        print(f"Error reserva: {e}")

        registrar_log(
            f"[ERROR] {e}"
        )

    # OPERACIÓN 10
    try:

        reserva1.cancelar()

        print("Reserva cancelada")

        registrar_log(
            "[INFO] Reserva cancelada"
        )

        operaciones += 1

    except ReservaError as e:

        print(e)

        registrar_log(
            f"[ERROR] {e}"
        )

    finally:

        registrar_log(
            "[INFO] Sistema finalizado"
        )

    print("=" * 50)
    print(f"Operaciones ejecutadas: {operaciones}")
    print("Sistema ejecutado correctamente")
    print("=" * 50)


if __name__ == "__main__":
    main()