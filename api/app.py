from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def get_data():
    data = {
        'diesel': '1.25 USD/L',
        'gasoline': '1.15 USD/L',
        'gas': '0.85 USD/L'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
