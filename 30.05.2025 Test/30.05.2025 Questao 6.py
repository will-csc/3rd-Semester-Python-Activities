"""6)
Desenvolva uma página “/adicionar” onde a página contém 
um campo para o usuário cadastrar itens e que serão 
adicionados em uma lista.”"""

# William C S de Carvalho
# RA 105637
# ADS3NC

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

itens = []

@app.route('/adicionar', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        item = request.form.get('item')
        if item:
            itens.append(item)
        return redirect(url_for('add'))
    return render_template('add.html', itens=itens)

if __name__ == '__main__':
    app.run(debug=True)


