from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # Домашняя страница
    return render_template('замени_меня.html')


@app.route('/contacts')
def contacts():
    # Контакты
    adress = 'Мой адресс'
    return render_template('замени_меня.html', adress=adress)


@app.route('/buy')
def buy():
    # Оформление заказа
    return render_template('замени_меня.html')


@app.route('/specialoffer')
def specialoffer():
    # Cтраница с акцией
    return render_template('замени_меня.html')

@app.route('/head')
def specialoffer():
    # Cтраница с акцией
    return render_template('head.html')
    
if __name__ == "__main__":
    app.run()
