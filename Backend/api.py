from flask import Flask, jsonify
from flask_cors import CORS
import copy

class API:
    def __init__(self, data, lock):
        self.data = data
        self.lock = lock
        self.app = Flask(__name__)
        CORS(self.app)

        @self.app.route('/data', methods=['GET'])
        def get_data():
            with self.lock:
                converted_data = {}
                for ip, port_tups, failed : self.data():
                    ports = []
                    for port, correct in port_tups:
                        ports.append({"port" : port, "correct" : correct})
                    converted_data[ip] = {{"ip" : ip},{"ports" : ports},{"failed" : failed}}
                return jsonify(self.data)
            
            
    def run(self):
        self.app.run(port=5000, host="0.0.0.0", debug=True)

if __name__ == '__main__':
    API()
