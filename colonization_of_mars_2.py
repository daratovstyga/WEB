from flask import Flask, url_for

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
