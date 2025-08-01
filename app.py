from flask import Flask, render_template, request, redirect
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def connect_db():
    return mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)


@app.route('/', methods=["GET", "POST"])
def form():
    if request.method == "POST":
        data = request.form["data"]
        historico = request.form["historico"]
        valor = request.form["valor"]
        conta = request.form["conta"]

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO lancamentos (data, historico, valor, conta)
            VALUES (%s, %s, %s, %s)
        """, (data, historico, valor, conta))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')

    return render_template("form.html")
