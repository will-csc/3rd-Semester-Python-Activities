"""5)
Faça uma rota “/fecaf” e ao executar a rota seja 
apresentada no navegador a mensagem “Bem-vindo(a)! 
A Universidade UniFecaf”"""

# William C S de Carvalho
# RA 105637
# ADS3NC

from flask import Flask

app = Flask(__name__)

@app.route('/fecaf')
def fecaf():
    return 'Bem-vindo(a)! A Universidade UniFecaf'

if __name__ == '__main__':
    app.run(debug=True)

