from flask import Flask, Blueprint, app, jsonify, request, abort
import json
from pathlib import Path
from routes import reservas_bp




app = Flask(__name__)



app.register_blueprint(reservas_bp)


@app.route('/health')
def health_check():
    return jsonify({"status": "ok", "entorno": "Listo"})
    

if __name__ == '__main__':
    app.run(debug=True)