from datos import salas, reservas


def listar_salas(capacidad_minima=None):
    if capacidad_minima is None:
        return salas
    return [sala for sala in salas if sala["capacidad"] >= capacidad_minima]


def buscar_sala_por_id(sala_id):
    return next((sala for sala in salas if sala["id"] == sala_id), None)


def crear_reserva(datos):
    sala = buscar_sala_por_id(datos["sala_id"])
    if sala is None:
        return None, "sala_no_encontrada"
    if datos["hora_fin"] <= datos["hora_inicio"]:
        return None, "horario_invalido"
    for reserva in reservas:
        if (reserva["sala_id"] == datos["sala_id"] and reserva["fecha"] == datos["fecha"]):
            if (datos["hora_inicio"] < reserva["hora_fin"] and datos["hora_fin"] > reserva["hora_inicio"]):
                return None, "horario_ocupado"
    nuevo_id = max((reserva["id"] for reserva in reservas), default=0) + 1
    nueva_reserva = {
        "id": nuevo_id,
        "sala_id": datos["sala_id"],
        "fecha": datos["fecha"],
        "hora_inicio": datos["hora_inicio"],
        "hora_fin": datos["hora_fin"],
        "responsable": datos["responsable"]
    }
    reservas.append(nueva_reserva)
    return nueva_reserva, None


def listar_reservas(sala_id=None):
    if sala_id is None:
        return reservas
    return [reserva for reserva in reservas if reserva["sala_id"] == sala_id]


def eliminar_reserva(reserva_id):
    reserva = next((reserva for reserva in reservas if reserva["id"] == reserva_id), None)
    if reserva is None:
        return False
    reservas.remove(reserva)
    return True