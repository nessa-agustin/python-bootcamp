from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return 'Hi, Welcome to my Page'
    return render_template('introduction.html')


@app.route('/hobby/')
@app.route('/hobbies/')
def hobby():
    hobbies = ['reading', 'running']
    return render_template('hobby.html', hobbies=hobbies)


@app.route('/opinion/<topic>')
@app.route('/opinions/<topic>')
def opinion(topic):
    return f'Let\'s talk about {topic}'


@app.route('/opinion/food/')
def opinion_food():
    foods = ['pasta', 'pizza', 'steak', 'bbq', 'clam chowder']
    return render_template('food.html', foods=foods)

@app.route('/skills/')
def skills():
    skills = {
        'Singing': 'Beginner',
        'Dancing': 'Beginner',
        'Cooking': 'Intermediate',
        'Driving': 'Intermediate',
        'Carpentry': 'Beginner',
    }

    return render_template('skills.html', skills=skills)


app.run()
