from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

mock_data = [
    {
        'ip': "192.168.1.2",
        'ports': [
            {
                'port': 22,
                'correct': True
            },
            {
                'port': 80,
                'correct': True
            }
        ],
        'failed': False
    },
    {
        'ip': "100.10.63.10",
        'ports': [
            {
                'port': 22,
                'correct': True
            },
            {
                'port': 80,
                'correct': False
            }
        ],
        'failed': False
    },
    {
        'ip': "172.1.2.1",
        'ports': [
            {
                'port': 22,
                'correct': True
            },
            {
                'port': 80,
                'correct': True
            },
            {
                'port': 443,
                'correct': True
            },
            {
                'port': 8080,
                'correct': True
            }
        ],
        'failed': True
    },
    {
        'ip': "172.1.2.3",
        'ports': [
            {
                'port': 22,
                'correct': True
            },
            {
                'port': 80,
                'correct': True
            },
            {
                'port': 443,
                'correct': True
            },
            {
                'port': 8080,
                'correct': False
            }
        ],
        'failed': False
    }
]

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(mock_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)