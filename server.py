import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/scan", methods=["GET"])
def scan_network():
  # Daftar perangkat contoh yang akan di-ping
  devices = [
      {"name": "Router Utama (Gateway)", "ip": "192.168.1.1"},
      {"name": "Switch Ruang Kasir", "ip": "192.168.1.2"},
      {"name": "Access Point Wi-Fi Tamu", "ip": "192.168.1.50"},
      {"name": "Server Lokal / Database", "ip": "192.168.1.100"},
  ]

  results = []
  for dev in devices:
    ip = dev["ip"]
    # Perintah ping (menggunakan -n 1 untuk Windows)
    response = os.system(f"ping -n 1 -w 200 {ip} >nul 2>&1")

    if response == 0:
      status = "ONLINE"
      # Simulasi latensi acak yang wajar untuk perangkat aktif
      ping_ms = "12 ms"
    else:
      status = "OFFLINE"
      ping_ms = "-"

    results.append({
        "name": dev["name"],
        "ip": ip,
        "status": status,
        "ping": ping_ms,
    })

  return jsonify(results)


if __name__ == "__main__":
  # Jalankan server lokal di port 5000
  app.run(debug=True, port=5000)