from flask import Flask, render_template, Response, request
from tinydb import TinyDB, Query
from datetime import datetime
import json
import logging

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

db = TinyDB("db.json")
app = Flask(__name__)

@app.route("/ping")
def ping():
    ip_ads = request.remote_addr    
    log_info = {
        "tempo": str(datetime.now()),
        "ip_ads": ip_ads,
        "acao": "ping",
        "parametros": {},
    }
    logger.info=(log_info)
    db.insert(log_info)
    return {"resposta": "pong"}

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    texto = data.get("dados")
    ip_ads = request.remote_addr    
    log_info = {
        "tempo": str(datetime.now()),
        "ip_ads": ip_ads,
        "acao": "echo",
        "parametros": data,
    }
    logger.info=(log_info)
    db.insert(log_info)
    return {"resposta": texto}

@app.route("/dash")
def dash():
    return render_template("index.html")

@app.route("/info")
def lista_logs():
    logs = db.all()
    logs_with_ids = [{"doc_id": log.doc_id, "data": log} for log in logs]
    return render_template("logs.html", logs=logs_with_ids)


