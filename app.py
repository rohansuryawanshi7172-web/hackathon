from flask import Flask
import threading
import time
from detection import get_data   # 👈 import your YOLO function

app = Flask(__name__)

people_count = 0
risk_level = "SAFE"


def run_detection():
    global people_count, risk_level

    while True:
        try:
            people_count, risk_level = get_data()

            print("Updated:", people_count, risk_level)

        except Exception as e:
            print("Error:", e)

        time.sleep(1)


@app.route('/')
def home():
    return "Crowd-Pulse Backend Running 🚀"


@app.route('/status')
def status():
    return {
        "people_count": people_count,
        "risk_level": risk_level
    }


if __name__ == "__main__":
    threading.Thread(target=run_detection, daemon=True).start()
    app.run(debug=True)
