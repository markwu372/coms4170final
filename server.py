import json
from sqlite3 import Timestamp
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
        "next_lesson" : "2", 
        # More to be added
        "p1": "https://www.capturelandscapes.com/wp-content/uploads/2017/10/Greenland-Husky-Rule-of-Thirds.jpg",
    
    "p2": "https://reyherphoto.com/wp-content/uploads/2016/11/rule-of-thirds-in-photography.jpg",
    "p3":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule1_counter1.jpeg?token=GHSAT0AAAAAABTPA73NZOFGTRLUMSGY75XGYS3ESQQ",
    "p4":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule1_counter2.jpeg?token=GHSAT0AAAAAABTPA73MAZEIUKZODHHA7OWWYS3ETBA",
    "description":"The rule of thirds is a way of dividing frames for optimal composition. It involves evenly dividing the frame between two equally spaced horizontal and vertical gridlines, creating a three-by-three grid. In order to create balance and flow within the image, compositional elements should be placed where these lines of the grid intersect or segment your image."
    },

    "2": {
        "lessons_id" : "2",
        "title" : "Leading Lines",
        "next_lesson" : "3",
        "p1":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule2_1.png?token=GHSAT0AAAAAABTPA73MRE2FMYB2CAHDDCJEYS3FEUQ",
        "p2":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule2_2.jpeg?token=GHSAT0AAAAAABTPA73M7W2ZTDK3BVB3B7UUYS3FE5Q",
        "p3":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule2_1_withline.png?token=GHSAT0AAAAAABTPA73MZIK3CWUHHJHQGLQ2YS3FFHQ",
        "p4":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule2_2_withline.jpeg?token=GHSAT0AAAAAABTPA73NENLEO3BS2JSH4DIUYS3FFOQ",
        "description":"Leading lines are visual elements that pull the viewer’s eye toward a subject or focal point. They can be anything — roads running off into the distance, an arm stretched out toward something else, tree branches rising toward the moon — anything that pulls attention toward something else. These lines can give flat surfaces the appearance of depth, dimension, and shape."

    },
    "3": {
        "lessons_id" : "3",
        "title" : "Balance",
        "next_lesson" : "4",
        "p1":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule3_1.jpeg?token=GHSAT0AAAAAABTPA73M5WE2YTGNDSYZ5DYIYS3FFVA",
        "p2":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule3_2.jpeg?token=GHSAT0AAAAAABTPA73M7IBHWGLNLVR2U3KCYS3FIJQ",
        "p3":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule3_1_withline.jpeg?token=GHSAT0AAAAAABTPA73MYEYRITSJ6TUJBNSGYS3FJYA",
        "p4":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule3_2_withline.jpeg?token=GHSAT0AAAAAABTPA73MD62TGDYI5FK7OA46YS3FJ7A",
        "description":"Balance is related to, but distinct from, symmetry. A balanced image doesn’t necessarily look the same right-to-left or side-to-side. Rather, the various quadrants of the image complement each other in aesthetically pleasing ways. Some photographers further explained this as symmetrical balance and asymmetrical balance. "
    },
    "4": {
        "lessons_id" : "4",
        "title" : "Diagonals",
        "next_lesson" : "5",
        "p1":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule4_1.jpeg?token=GHSAT0AAAAAABTPA73MNHSWMWD4ZC5A4BZYYS3FKIQ",
        "p2":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule4_2.png",
        "p3":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule4_1_withline.jpeg",
        "p4":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule4_2_withline.png",
        "description":"You can use the diagonal lines in the scene to compose frames. The diagonal lines tend to produce strong images than the horizontal and vertical lines. The diagonal which connects the opposite corners of the frame may not be used. It will not help to create beautiful images. "
    }, 
    "5": {
        "lessons_id" : "5",
        "title" : "Frames",
        "next_lesson" : "quiz1" ,#End of lessons, Go to Quiz 1
        "p1":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule5_1.jpeg",
        "p2":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule5_2.jpeg",
        "p3":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule5_1_withline.jpeg",
        "p4":"https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/rule5_2_withline.jpeg",
        "description":"Also called sub-framing, this type of compositional technique involves using or adding frame elements to emphasize and lead the viewer's eye towards your subject or to simply add interest to your image. It can be anything from natural frames like rock formations or man-made ones like windows and tunnels. it helps bring focus to your intended subject, it’s bound to create a more aesthetically-pleasing image."
    }
}

quiz_data = {
    "1": {
        "quiz_id": "1",
        "quiz_progress": 16.6,
        "title": "Problem 1",
        "next_lesson": "2",
        "img": "https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/quiz1.png",
        "solution": "https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/quiz1_sol.png",
        "answer": "frames",
        "learning_url": "../lessons/5"
    },
    "2": {
        "quiz_id": "2",
        "title": "Problem 2",
        "quiz_progress": 33.3,
        "next_lesson": "3",
        "img": "https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/quiz2.jpeg",
        "solution": "https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/quiz2_sol.jpeg",
        "answer": "rule_of_thirds",
        "learning_url": "../lessons/1"
    },
    "3": {
        "quiz_id": "3",
        "title": "Problem 3",
        "quiz_progress": 50.0,
        "next_lesson": "4",
        "img": "https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/quiz3.jpeg",
        "solution": "https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/quiz3_sol.jpeg",
        "answer": "diagonals",
        "learning_url": "../lessons/4"
    },
    "4": {
        "quiz_id": "4",
        "quiz_progress": 66.7,
        "title": "Problem 4",
        "next_lesson": "5",
        "img": "https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/quiz4_sol.png",
        "solution": "https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/quiz4.png",
        "answer": "leading_lines",
        "learning_url": "../lessons/2"
    },
    "5": {
        "quiz_id": "5",
        "quiz_progress": 83.3,
        "title": "Problem 5",
        "next_lesson": "6",
        "img": "https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/quiz5.jpeg",
        "solution": "https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/quiz5_sol.jpeg",
        "answer": "balance",
        "learning_url": "../lessons/3"
    },
    "6": {
        "quiz_id": "6",
        "quiz_progress": 100,
        "title": "Problem 6",
        "next_lesson": "",
        "img": "https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/quiz6.jpeg",
        "solution": "https://raw.githubusercontent.com/markwu372/coms4170final/main/data/images/quiz6_sol.jpeg",
        "answer": "leading_lines",
        "learning_url": "../lessons/2"
    }


}


correct_number = 0
recommend_list = []
quiz_anwsers = []
timestamp = []

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

@app.route('/timestamp', methods=['GET', 'POST'])
def add_time():
    global timestamp
    item = request.get_json()
    timestamp.append(item['time'])
    return jsonify(item=None)

@app.route('/quiz/correct', methods=['GET', 'POST'])
def add_correct():
    global correct_number
    global recommend_list

    item = request.get_json()
    quiz_anwsers.append(item['topic'])
    if item['correct'] == '1':
        correct_number += 1
    else:
        if item['topic'] not in recommend_list:
            recommend_list.append(item['topic'])
    return jsonify(item=None)


@app.route('/report')
def report():
    print(quiz_anwsers)
    print(timestamp)
    return render_template('report.html', correct=correct_number, topic=recommend_list)


if __name__ == '__main__':
   app.run(debug = True)