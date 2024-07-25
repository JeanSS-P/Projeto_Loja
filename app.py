from flask import Flask, request, jsonify, render_template, redirect, url_for
from sistema_de_vendas import SistemaDeVendas
from cliente import Cliente

app = Flask("__main__")
sistema = SistemaDeVendas()

# Adicionando alguns hambúrgueres ao menu
sistema.adicionar_hamburguer_ao_menu("Cheeseburger", 12.50)
sistema.adicionar_hamburguer_ao_menu("Hamburger", 10.00)
sistema.adicionar_hamburguer_ao_menu("Bacon Burger", 14.00)
sistema.adicionar_hamburguer_ao_menu("Veggie Burger", 11.00)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    menu = sistema.mostrar_menu()
    return render_template('menu.html', menu=menu)


@app.route('/cliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method== 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        n_residencial = request.form['n_residencial']
        cep = request.form['cep']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        novo_clinete = Cliente(nome,cpf,n_residencial, cep, endereco, telefone)
        sistema.adicionar_cliente(novo_cliente)
        return redirect(url_for('index'))
    return render_template('cliente.html')
        
  

if __name__ == "__main__":

    app.run(debug=True)
