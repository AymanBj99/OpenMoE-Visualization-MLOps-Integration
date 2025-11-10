from flask import Flask, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/router_analysis.csv')
def get_router_csv():
    csv_path = os.path.join("data", "router_analysis.csv")
    if os.path.exists(csv_path):
        return send_file(csv_path, mimetype='text/csv')
    else:
        return "Fichier non trouvé. Exécute d'abord analyze_router.py.", 404

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5500, debug=True)

