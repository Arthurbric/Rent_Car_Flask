from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login_form():
   return render_template('index.html')

@app.route('/pass', methods=['GET'])
def process_login():
   user = request.args.get('user')
   senha = request.args.get('senha')

   # Faça o processamento necessário com os valores recebidos
   # Neste exemplo, vamos apenas retornar os valores dentro de uma função
   if user == 'Guilherme' and senha == '123':
       return render_template('pass.html',nome = user)
   else:
       return render_template('index.html')

if __name__ == '__main__':
   app.run()
