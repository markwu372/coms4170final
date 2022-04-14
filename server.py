import json
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)
import copy

homepage_data = {
    "description": "Photo composition is how a photographer arranges visual elements within their frame. “It’s a pleasing organization of objects within your rectangle,” says photographer Adam Long. Putting subjects or scenes inside that space may sound easy, yet it’s anything but. Composition in your shots can often be difficult and it’s always important. “Everything can seem perfect: lighting, location, wardrobe, styling, whatever,” says photographer Grace Rivera. “But if your composition is off, that’s a deal breaker.”",
    "rules": ["Rules of Thirds", "Leading Lines", "Balance", "Diagonals", "Frames"]
}

lessons_data = {
    # Test data for learning pages
    "1": {
        "lessons_id" : "1",
        "title" : "Rules of Thirds",
        "next_lesson" : "2"
        # More to be add
    },
    "2": {
        "lessons_id" : "2",
        "title" : "Leading Lines",
        "next_lesson" : "3"
    },
    "3": {
        "lessons_id" : "3",
        "title" : "Balance",
        "next_lesson" : "4"
    },
    "4": {
        "lessons_id" : "4",
        "title" : "Diagonals",
        "next_lesson" : "5"
    }, 
    "5": {
        "lessons_id" : "5",
        "title" : "Frames",
        "next_lesson" : "quiz1" #End of lessons, Go to Quiz 1
    }
}

quiz_data = {
    # Test data for quiz pages
    "1": {
        "quiz_id": "1",
        "title": "Problem1",
        "next_quiz": "2"
        # More to be add
    }
}

@app.route('/')
def homepage():
   return render_template('homepage.html', homepage_data=homepage_data)

@app.route('/home')
def home():
   return render_template('homepage.html', homepage_data=homepage_data)

@app.route('/lessons/<id>')
def lessons(id=None):
    return render_template('lessons.html', lessons_data=lessons_data[id])

@app.route('/quiz/<id>')
def quiz(id=None):
    return render_template('quiz.html', quiz_data=quiz_data[id])

if __name__ == '__main__':
   app.run(debug = True)