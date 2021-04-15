from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof.lower())


@app.route('/list_prof/<list>')
def list_prof(list):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
    return render_template('list_prof.html', prof=professions, type=list)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    profil = {}
    profil['title'] = 'Анкета'
    profil['surname'] = 'Watny'
    profil['name'] = 'Mark'
    profil['education'] = 'выше среднего'
    profil['profession'] = 'штурман марсохода'
    profil['sex'] = 'male'
    profil['motivation'] = 'Всегда мечтал застрять на марсе!'
    profil['ready'] = 'True'
    return render_template('auto_answer.html', **profil)


@app.route('/distribution')
def distribution():
    list_of_astro = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', astro=list_of_astro)


@app.route('/table/<sex>/<age>')
def table(sex, age):
    return render_template('table.html', sex=sex, age=int(age))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')