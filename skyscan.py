import http.client
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_timetable():
    conn = http.client.HTTPSConnection("timetable-lookup.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "f97e3dbab8mshb83b4a869cc05bbp1448fajsna77ddd7b5e76",
        'X-RapidAPI-Host': "timetable-lookup.p.rapidapi.com"
    }

    conn.request("GET", "/TimeTable/STN/ARN/20230614/?Airline=FR", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

if __name__ == '__main__':
    app.run()
