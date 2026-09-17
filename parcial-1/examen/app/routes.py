from flask import Blueprint, jsonify, request, abort
import servicio


reservas_bp = Blueprint("reservas", __name__)

@reservas_bp.route("/api/salas", methods=["GET"])
def listar_salas():
    capacidad_minima = request.args.get("capacidad_minima", type=int)
    salas = servicio.listar_salas(capacidad_minima)
    return jsonify({"salas": salas})


@reservas_bp.route("/api/salas/<int:sala_id>", methods=["GET"])
def obtener_sala(sala_id):
    sala = servicio.buscar_sala_por_id(sala_id)
    if sala is None:
        abort(404, description="Sala no encontrada")
    return jsonify(sala)


@reservas_bp.route("/api/reservas", methods=["POST"])
def crear_reserva():
    datos = request.get_json(silent=True)
    campos_obligatorios = [
        "sala_id",
        "fecha",
        "hora_inicio",
        "hora_fin",
        "responsable"
    ]
    print(datos)
    if not isinstance(datos, dict):
        abort(400, description="El cuerpo de la petición debe ser JSON")
    for campo in campos_obligatorios:
        if campo not in datos:
            abort(400, description=f"Falta el campo obligatorio: {campo}")

    reserva, error = servicio.crear_reserva(datos)
    if error == "sala_no_encontrada":
        abort(404, description="La sala no existe")
    if error == "horario_invalido":
        abort(400, description="hora_fin debe ser posterior a hora_inicio")
    if error == "horario_ocupado":
        abort(description="La sala ya tiene una reserva en ese horario")
    return jsonify(reserva), 201


@reservas_bp.route("/api/reservas", methods=["GET"])
def listar_reservas():
    sala_id = request.args.get("sala_id", type=int)
    reservas = servicio.listar_reservas(sala_id)
    return jsonify({"reservas": reservas})


@reservas_bp.route("/api/reservas/<int:reserva_id>", methods=["DELETE"])
def cancelar_reserva(reserva_id):
    eliminado = servicio.eliminar_reserva(reserva_id)

    if not eliminado:
        abort(404, description="Reserva no encontrada")
    return jsonify({"mensaje": "Reserva eliminada"}), 204
