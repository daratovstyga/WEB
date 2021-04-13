from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def mission_name():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    p_list = ['Человечество вырастает из детства.',
              'Человечеству мала одна планета.',
              'Мы сделаем обитаемыми безжизненные пока планеты.',
              'И начнем с Марса!',
              'Присоединяйся!']
    return "</br>".join(p_list)


@app.route('/image_mars')
def image():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars-planet-clip-art-15.png')}" width= "400" height="400">
                        <p>Вот она какая, красная планета.</p>
                      </body>
                    </html>'''


@app.route('/promotion_image')
def promotion_image():
    p_list = ['Человечество вырастает из детства.',
              'Человечеству мала одна планета.',
              'Мы сделаем обитаемыми безжизненные пока планеты.',
              'И начнем с Марса!',
              'Присоединяйся!']
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
                        rel="stylesheet"
                        integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars-planet-clip-art-15.png')}" width= "400" height="400">
                        <div class="alert alert-primary" role="alert">
                          <br>{p_list[0]}
                        </div>
                        <div class="alert alert-success" role="alert">
                          <br>{p_list[1]}
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          <br>{p_list[2]}
                        </div>
                        <div class="alert alert-warning" role="alert">
                          <br>{p_list[3]}
                        </div>
                        <div class="alert alert-danger" role="alert">
                          <br>{p_list[4]}
                        </div>
                      </body>
                      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
                    </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
                            rel="stylesheet"
                            integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
                            crossorigin="anonymous">
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <div class="p-3 mb-2 bg-primary text-white"></div>
                            <div class="mx-auto" style="width: 320px;">
                              <h2>Анкета претендента</h2>
                            </div>
                            <div class="mx-auto" style="width: 280px;">
                                <h3>на участие в миссии</h3>
                            </div>
                            <form class="login_form" method="post">
                            <div class="mx-auto" style="width: 380px;">
                              <div class="p-2 bg-dark text-white border"><label>
                                <div class="input-group mb-3">
                                  <input type="text" class="form-control" placeholder="Введите фамилию" name="surname">
                                </div>
                                <div class="input-group mb-3">
                                  <input type="text" class="form-control" placeholder="Введите имя" name="name">
                                </div>
                                <div class="input-group mb-3">
                                  <input type="text" class="form-control" placeholder="Введите адрес почты" name="email">
                                </div>
                                <label for="basic-url" class="form-label">Какое у Вас образование?</label>
                                <select class="form-select" aria-label="Пример выбора по умолчанию" name="education">
                                  <option selected>Начальное</option>
                                  <option value="1">Среднее</option>
                                  <option value="2">Высшее</option>
                                </select>
                                <label for="basic-url" class="form-label">Какие у Вас есть профессии?</label>
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" name="professions" id="flexCheckDefault">
                                  <label class="form-check-label" for="flexCheckChecked">
                                    Инженер-исследователь
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" name="professions" id="flexCheckDefault">
                                  <label class="form-check-label" for="flexCheckChecked">
                                    Инженер-строитель
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" name="professions" id="flexCheckDefault">
                                  <label class="form-check-label" for="flexCheckChecked">
                                    Пилот
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" name="professions" id="flexCheckDefault">
                                  <label class="form-check-label" for="flexCheckChecked">
                                    Метеоролог
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" name="professions" id="flexCheckDefault">
                                  <label class="form-check-label" for="flexCheckChecked">
                                    Инженер по жизнеобеспечению
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" name="professions" id="flexCheckDefault">
                                  <label class="form-check-label" for="flexCheckChecked">
                                    Инженер по радиационной защите
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" name="professions" id="flexCheckDefault">
                                  <label class="form-check-label" for="flexCheckChecked">
                                    Врач
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" name="professions" id="flexCheckDefault">
                                  <label class="form-check-label" for="flexCheckChecked">
                                    Экзобиолог
                                  </label>
                                </div>
                                <label for="basic-url" class="form-label">Укажите пол</label>
                                <div class="form-check">
                                  <input class="form-check-input" type="radio" name="sex" id="flexRadioDefault2" checked>
                                  <label class="form-check-label" for="flexRadioDefault2">
                                    Мужской
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="radio" name="sex" id="flexRadioDefault1">
                                  <label class="form-check-label" for="flexRadioDefault1">
                                    Женский
                                  </label>
                                </div>
                                <label for="basic-url" class="form-label">Почему Вы хотите принять участие в миссии?</label>
                                <div class="input-group">
                                  <textarea class="form-control" aria-label="С текстовым полем" name="about"></textarea>
                                </div>
                                <label for="basic-url" class="form-label">Приложите фотографию</label>
                                <div class="input-group mb-3">
                                  <input type="file" class="form-control" id="inputGroupFile02" name="file">
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="accept">
                                  <label class="form-check-label" for="flexCheckDefault">
                                    Готовы остаться на Марсе?
                                  </label>
                                </div>
                                <div class="col-12">
                                  <button type="submit" class="btn btn-primary">Отправить</button>
                                </div>
                              </label></div>
                            </div>
                            </form>
                          </body>
                          <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/choice/Марс')
def mars():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
                        rel="stylesheet"
                        integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: Марс!</h1>
                        <h2>Марс - лучшая планета!</h2>
                        <div class="alert alert-primary" role="alert">
                          <br>Всё
                        </div>
                        <div class="alert alert-success" role="alert">
                          <br>Супер
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          <br>Круто
                        </div>
                        <div class="alert alert-warning" role="alert">
                          <br>Классно
                        </div>
                        <div class="alert alert-danger" role="alert">
                          <br>И красиво
                        </div>
                      </body>
                      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
                    </html>'''


@app.route('/choice/Юпитер')
def jupiter():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
                        rel="stylesheet"
                        integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: Юпитер!</h1>
                        <h2>Юпитер - лучший газовый гигант!</h2>
                        <div class="alert alert-primary" role="alert">
                          <br>Всё
                        </div>
                        <div class="alert alert-success" role="alert">
                          <br>Супер
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          <br>Круто
                        </div>
                        <div class="alert alert-warning" role="alert">
                          <br>Классно
                        </div>
                        <div class="alert alert-danger" role="alert">
                          <br>Это ловушка
                        </div>
                      </body>
                      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
                    </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
                        rel="stylesheet"
                        integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
                        crossorigin="anonymous">
                        <title>Результаты</title>
                      </head>
                      <body>
                        <h1>Результат отбора</h1>
                        <h2>Претендента на участие в миссии {nickname}:</h2>
                        <div class="alert alert-success" role="alert">
                          <br>Поздравляем! Ваш рейтинг после {level} этапа отбора
                        </div>
                        <div class="alert alert-light" role="alert">
                          <br>составляет {rating}!
                        </div>
                        <div class="alert alert-warning" role="alert">
                          <br>Желаем удачи!
                        </div>
                      </body>
                      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
                    </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                 <link rel="stylesheet"
                                 href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                 integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                 crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/new_style.css')}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <div class="mx-auto" style="width: 480px;">
                                  <h1>Загрузка фотографии</h1>
                                </div>
                                <div class="mx-auto" style="width: 380px;">
                                  <h3>для участия в миссии</h3>
                                </div>
                                <form method="post" enctype="multipart/form-data">
                                <div class="mx-auto" style="width: 460px;">
                                   <div class="p-2 bg-dark text-white border"><label>
                                   <label for="basic-url" class="form-label">Приложите фотографию</label>
                                   <div class="form-group">
                                        <label for="photo"></label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                    </label></div>
                                </div>
                                </form>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        with open('static/img/new_img.png', 'wb') as file:
            file.write(f.read())
        return f'''<!doctype html>
                                    <html lang="en">
                                      <head>
                                        <meta charset="utf-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                         <link rel="stylesheet"
                                         href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                         integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                         crossorigin="anonymous">
                                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/new_style.css')}" />
                                        <title>Отбор астронавтов</title>
                                      </head>
                                      <body>
                                        <div class="mx-auto" style="width: 480px;">
                                          <h1>Загрузка фотографии</h1>
                                        </div>
                                        <div class="mx-auto" style="width: 380px;">
                                          <h3>для участия в миссии</h3>
                                        </div>
                                        <form method="post" enctype="multipart/form-data">
                                        <div class="mx-auto" style="width: 480px;">
                                           <div class="p-2 bg-dark text-white border"><label>
                                           <label for="basic-url" class="form-label">Приложите фотографию</label>
                                           <div class="form-group">
                                                <label for="photo"></label>
                                                <input type="file" class="form-control-file" id="photo" name="file">
                                            </div>
                                            <img src="{url_for('static', filename='img/new_img.png')}" width= "400" height="400">
                                            <button type="submit" class="btn btn-primary">Отправить</button>
                                            </label></div>
                                        </div>
                                        </form>
                                      </body>
                                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
