# Decisiones de diseño

Nombre: Jesus Manuel Ruiz Fuentes
Fecha: 17 de septiembre de 2026

Responde honestamente. Se evalúa la solidez del argumento, no la extensión.

---

## 1. Diseño de URIs

Justifica el diseño de tus URIs. ¿Qué ventaja y qué desventaja tendría exponer
las reservas de forma anidada, como `/api/salas/<id>/reservas`, en lugar del
diseño que usaste?

*(tu respuesta)*

Utilice `/api/salas` para consultar las salas y `/api/salas/<id>` para consultar una sala especifica. Para las reservas utilice `/api/reservas` para crearlas y consultarlas, y `/api/reservas/<id>` para eliminarlas.

Los filtros `capacidad_minima` se manejan como parametros para hacer una consulta con este

No considere utilizar `/api/salas/<id>/reservas`, para mantenerlos a ambos como un recurso independiente y estos pueden consultarse directamente

La ventaja de utilizar rutas anidadas seria que expresan de una froma mas clara la realacion que hay entre ellas 
La desventaja es que seria menos practico para operaciones en las que se quieren consultar todas las reservas o trabajar directamente con una reserva especifica
---

## 2. Códigos de estado

Enumera qué código devuelve cada uno de tus cinco endpoints, tanto en el caso
exitoso como en cada caso de error que hayas contemplado. Después elige uno de
ellos y explica a fondo por qué ese código y no otro parecido.

| Endpoint | Éxito | Errores contemplados |
|---|---|---|
|Listar Salas | 200 | 404 |
|Obtener Sala Id | 200 | 404 |
|Crear Reserva | 201 | 404, 500|
|Listar reserva | 200  | 40# Decisiones de diseño

Nombre: Jesus Manuel Ruiz Fuentes
Fecha: 17 de septiembre de 2026

Responde honestamente. Se evalúa la solidez del argumento, no la extensión.

---

## 1. Diseño de URIs

Justifica el diseño de tus URIs. ¿Qué ventaja y qué desventaja tendría exponer
las reservas de forma anidada, como `/api/salas/<id>/reservas`, en lugar del
diseño que usaste?

*(tu respuesta)*

Utilice `/api/salas` para consultar las salas y `/api/salas/<id>` para consultar una sala especifica. Para las reservas utilice `/api/reservas` para crearlas y consultarlas, y `/api/reservas/<id>` para eliminarlas.

Los filtros `capacidad_minima` se manejan como parametros para hacer una consulta con este

No considere utilizar `/api/salas/<id>/reservas`, para mantenerlos a ambos como un recurso independiente y estos pueden consultarse directamente

La ventaja de utilizar rutas anidadas seria que expresan de una froma mas clara la realacion que hay entre ellas 
La desventaja es que seria menos practico para operaciones en las que se quieren consultar todas las reservas o trabajar directamente con una reserva especifica
---

## 2. Códigos de estado

Enumera qué código devuelve cada uno de tus cinco endpoints, tanto en el caso
exitoso como en cada caso de error que hayas contemplado. Después elige uno de
ellos y explica a fondo por qué ese código y no otro parecido.

| Endpoint | Éxito | Errores contemplados |
|---|---|---|
|Listar Salas | 200 | 404 |
|Obtener Sala Id | 200 | 404 |
|Crear Reserva | 201 | 400, 404, 500|
|Listar reserva | 200  | 404 |
|Eliminar Reserva |204  | 404 |

Explicación a fondo del código elegido:

*(tu respuesta)*

---

## 3. Petición repetida

Si el cliente envía exactamente la misma petición de creación de reserva dos
veces seguidas, ¿qué ocurre con tu implementación? ¿Ese comportamiento es el
correcto para este dominio? Argumenta.

*(tu respuesta)*

Da un error 500, y funciona con un abort, devuleve una alerta que dice que la sala ya tiene una reservahecha en ese horario, lo cual considero que es correcto
---

## 4. Separación de responsabilidades

Señala una línea o bloque concreto de tu `servicio.py` y explica por qué estaría
mal colocado en `routes.py`. Haz lo inverso con una línea de `routes.py`.

*(tu respuesta)*
```bash
if (
    datos["hora_inicio"] < reserva["hora_fin"]
    and datos["hora_fin"] > reserva["hora_inicio"]
):
    return None, "horario_ocupado"
```4 |
|Eliminar Reserva |204  | 404 |

Explicación a fondo del código elegido:

*(tu respuesta)*

---

## 3. Petición repetida

Si el cliente envía exactamente la misma petición de creación de reserva dos
veces seguidas, ¿qué ocurre con tu implementación? ¿Ese comportamiento es el
correcto para este dominio? Argumenta.

*(tu respuesta)*

Da un error 500, y funciona con un abort, devuleve una alerta que dice que la sala ya tiene una reservahecha en ese horario, lo cual considero que es correcto
---

## 4. Separación de responsabilidades

Señala una línea o bloque concreto de tu `servicio.py` y explica por qué estaría
mal colocado en `routes.py`. Haz lo inverso con una línea de `routes.py`.

*(tu respuesta)*
```bash
if (
    datos["hora_inicio"] < reserva["hora_fin"]
    and datos["hora_fin"] > reserva["hora_inicio"]
):
    return None, "horario_ocupado"
```
Estaria mal en roytes ya que estto es una regla de negocio (el horario disponible de las salas) por lo que services debe manejar esto, y route solo manejar las peticiones http y llamas a service