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


   def login_data(username, password):
       if username == 'guilherme' and password == '123':
           return f'Username: {username}, Password: {password}'
       else:
           return render_template('index.html')




   result = login_data(user, senha)
   return result




if __name__ == '__main__':
   app.run()

