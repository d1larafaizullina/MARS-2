"""
Решение задач:
WEB. Шаблоны. flask-wtf
"""


from flask import Flask, render_template


app = Flask(__name__)


# 1 Готовимся к миссии
@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


# 3 Список профессий
@app.route("/list_prof/<string:_list>")
def list_prof(_list):
    profs = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог',
             'врач', 'инженер по терраформированию', 'климатолог',
             'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
             'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода',
             'киберинженер', 'штурман', 'пилот дронов']
    return render_template('list_prof.html', _list=_list, profs=profs)


# 4 Автоматический ответ
@app.route("/answer")
@app.route("/auto_answer")
def auto_answer():
    param = {'title': 'Астронавт', 'surname': 'Watny', 'name': 'Mark',
             'education': 'выше среднего', 'profession': 'штурман марсохода',
             'sex': 'male', 'motivation': 'Всегда мечтал застрять на Марсе!',
             'ready': True}
    return render_template('auto_answer.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
