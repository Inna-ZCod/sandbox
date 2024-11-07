from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Получаем текущие дату и время
    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y %H:%M:%S")
    # Возвращаем HTML-страницу с текущими датой и временем
    return f"<h1>Текущие дата и время: {current_time}</h1>"

if __name__ == "__main__":
    app.run()