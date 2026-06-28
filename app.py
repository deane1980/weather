from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/temp')
def get_cam_temp():
    try:
        # Fetch the plain text file directly
        url = "https://www.cl.cam.ac.uk/weather/current/index.txt"
        response = requests.get(url, timeout=10)
        
        # Parse the text lines
        for line in response.text.splitlines():
            if line.startswith("temperature="):
                # Extract just the number after the '='
                temp_value = line.split("=")[1].strip()
                return jsonify({"temp": temp_value})
                
        return jsonify({"temp": "N/A"})
    except Exception as e:
        return jsonify({"temp": "Error", "details": str(e)})

if __name__ == '__main__':
    app.run()
