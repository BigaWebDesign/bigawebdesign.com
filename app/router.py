from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/hakkimizda')
def hakkimizda():
    return render_template('pages/hakkimizda.html')

@app.route('/referanslar')
def referanslar():
    return render_template('pages/referanslar.html')

@app.route('/web-paketleri')
def webpaketleri():
    return render_template('pages/web-paketleri.html')

@app.errorhandler(404)
def sayfa_bulunamadi(e):
    return render_template('err/404.html'), 404

@app.errorhandler(500)
def ic_sunucu_hatası(e):
    return render_template('err/500.html'), 500
