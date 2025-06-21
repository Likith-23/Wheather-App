from flask import Flask, request, render_template_string
import requests 
app = Flask(__name__)
API_key = "bc14c8c5e4960d560848e37ccbc76180"
HTML_template = """<html>
<head>
<title>
Weather App
</title>
</head>
<body>
<h1>Weather Prediction app</h1>
<form method="post">
<input type="text" name="city" placeholder="enter city name" required>
<button type="submit">Get Weather!</button>
</form>
{% if weather %}
<h2>weather in {{weather.city}}</h2>
<p>Temperature: {{weather.temperature}} C</p>
<p>Description: {{weather.description}} </p>
<img src="http://openweathermap.org/img/wn/{{ weather.icon }}@2x.png" alt="Weather Icon">
{% endif %}
</body>
</html>
"""
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data['name'], 
            "temperature": data['main']['temp'],
            "description": data['weather'][0]['description'], 
            "icon": data['weather'][0]['icon']
        }
    else:
        return None
@app.route("/", methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get('city')
        if city:
            weather_data = get_weather(city)
    return render_template_string(HTML_template, weather=weather_data)
if __name__ == "__main__":
    app.run(debug=True)
    
    
hello = input('hi?')
    