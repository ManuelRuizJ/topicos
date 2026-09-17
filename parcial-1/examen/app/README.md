# Esqueleto: API de reservas de salas

## Levantar el proyecto

Windows:

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

macOS y Linux:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Verificar que funciona

Con el servidor corriendo, abre en el navegador o en tu cliente HTTP:

```
http://127.0.0.1:5000/health
```

Debe responder `{"estado": "ok"}` con código 200. Si esto funciona, tu entorno
está listo. Hazlo antes de escribir cualquier línea de código.

## Archivos

- `app.py`: crea la aplicación. Aquí registras tu blueprint.
- `routes.py`: capa HTTP. Vacío, lo escribes tú.
- `servicio.py`: lógica de negocio. Vacío, lo escribes tú.
- `datos.py`: salas precargadas y lista de reservas en memoria.
- `DECISIONES.md`: preguntas a responder. Forma parte de la entrega.

## Entrega

Comprime la carpeta completa sin la carpeta `venv` y súbela a Moodle como
`Examen1_Reservas_TuNombre.zip`.
