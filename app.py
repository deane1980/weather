from flask import Flask, jsonify
import requests

app = Flask(__name__)

# The correct, live Cambridge weather text URL
CAM_WEATHER_TXT_URL = "https://www.cl.cam.ac.uk/weather/txt/weather.txt"

def parse_weather_text(text_data):
    weather_dict = {}
    lines = text_data.strip().split('\n')
    
    for line in lines:
        if '=' in line:
            key, value = line.split('=', 1)
            weather_dict[key.strip()] = value.strip()
            
    return weather_dict

@app.route('/temp')
def get_cam_temp():
    try:
        response = requests.get(CAM_WEATHER_TXT_URL, timeout=10)
        response.raise_for_status()
        
        raw_data = parse_weather_text(response.text)
        
        # Pulls the correct temperature key from the new text file
        temp_value = raw_data.get('temperature', 'N/A')
        
        return jsonify({"temp": temp_value})
    except Exception as e:
        return jsonify({"temp": "Error", "details": str(e)})

if __name__ == '__main__':
    app.run()
