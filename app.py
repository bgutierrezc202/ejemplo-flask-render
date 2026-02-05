import os
from flask import Flask, jsonify

app = Flask(__name__)

# Variables de entorno (con valores por defecto para evitar crashes)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret")
app.config["APP_ENV"] = os.environ.get("APP_ENV", "development")

@app.get("/")
def home():
    return jsonify(
        message="Hola desde Flask en Render",
        app_env=app.config["APP_ENV"]
    )

# Importante para Render: escuchar el puerto que Render expone (PORT)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))  # Render usa 10000 por defecto
    app.run(host="0.0.0.0", port=port)
