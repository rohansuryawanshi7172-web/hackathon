from flask import Flask
import threading
import time

app = Flask(__name__)

# 🔴 Shared data (IMPORTANT)
people_count = 0
risk_level = "SAFE"

def run_detection():
    global people_count, risk_level

    while True:
        # Simulated values (replace later with real data)
        people_count += 1

        if people_count <= 2:
            risk_level = "SAFE"
        elif people_count <= 5:
            risk_level = "CAUTION"
        else:
            risk_level = "CRITICAL"

        print("Updated:", people_count, risk_level)

        time.sleep(2)

@app.route('/status')
def status():
    return {
        "people_count": people_count,
        "risk_level": risk_level
    }

if __name__ == "__main__":
    threading.Thread(target=run_detection).start()
    app.run(debug=True)