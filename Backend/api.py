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
            converted_data = {}
            with self.lock:
                data_copy = copy.deepcopy(self.data)
            for key, value in data_copy.items():
                ports, failed, connected = value
                converted_ports = []
                for port, correct in ports:
                    converted_ports.append({"port" : port, "correct" : correct})
                converted_data[key] = {"ip" : key, "ports" : converted_ports, "failed" : failed, "connected" : connected}
                print(converted_data)
            return jsonify(converted_data)
            
            
    def run(self):
        self.app.run(debug=True, port=5000, host='0.0.0.0')

if __name__ == '__main__':
    API()
