from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/pass', methods=['GET'])
def check():

  nome=str(request.form['user'])
  cpf=str(request.form['senha'])

  if nome == "Arthur" or cpf == "1234" :
    return render_template('pass.html', nome)
  return render_template('pass.html')
app.run(debug=1)