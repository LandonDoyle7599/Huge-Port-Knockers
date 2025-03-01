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
        'authenticated': False
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
        'authenticated': False
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
        'authenticated': True
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
        'authenticated': False
    }
]

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(mock_data)

if __name__ == '__main__':
    app.run(debug=True)