from flask import Flask, render_template, Response
import requests
import camera
from camera import Video, choice, total_headgears

app=Flask(__name__)

camera.choice = 0

@app.route('/')
def index():
    #global ch
    return render_template('index.html')

@app.route('/culturalNews.html')
def culturalNews():
    url = ('https://newsapi.org/v2/everything?'
           'q=festival&'
           'from=2022-10-26&'
           'sortBy=popularity&'
           'language=en&'
           'apiKey=8d9dec18335e4d82b8d31756136ebc10')
    r = requests.get(url).json()
    case = {
        'articles' : r['articles']
    }
    return render_template("culturalNews.html", cases = case)

@app.route('/start.html')
def start_the_quiz():
    return render_template("start.html")

@app.route('/quiz.html')
def quiz_live():
    return render_template("quiz.html")

@app.route('/end.html')
def quiz_end():
    return render_template("end.html")


@app.route('/background_process_test')
def background_process_test():
    camera.choice = (camera.choice+1) % camera.total_headgears
    #global ch
    #ch = (ch + 1) % camera.total_headgears
    return ("nothing")


def gen(camera):
    #choice = 1
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')

@app.route('/video')

def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(debug=True)
