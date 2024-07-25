from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sistema_de_vendas import SistemaDeVendas
from cliente import Cliente

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto_loja_hamburguer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
sistema = SistemaDeVendas()

# Modelo de Cliente para o banco de dados
class ClienteModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    n_residencial = db.Column(db.String(10), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)

# Modelo de Venda para o banco de dados
class VendaModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente_model.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)

    cliente = db.relationship('ClienteModel', backref=db.backref('vendas', lazy=True))

# Criação do banco de dados
with app.app_context():
    db.create_all()

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
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        cep = request.form['cep']
        n_residencial = request.form['n_residencial']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        novo_cliente = ClienteModel(nome=nome, cpf=cpf, cep=cep, n_residencial=n_residencial, endereco=endereco, telefone=telefone)
        db.session.add(novo_cliente)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('cliente.html')

@app.route('/pedido', methods=['GET', 'POST'])
def iniciar_pedido():
    if request.method == 'POST':
        cpf = request.form['cpf']
        cliente = ClienteModel.query.filter_by(cpf=cpf).first()
        if cliente:
            sistema.iniciar_pedido(cliente)
            return redirect(url_for('menu'))
        else:
            return "Cliente não encontrado.", 404
    return render_template('pedido.html')

@app.route('/adicionar_item', methods=['POST'])
def adicionar_item():
    indice = int(request.form['indice'])
    mensagem = sistema.adicionar_ao_pedido(indice)
    return redirect(url_for('menu'))

@app.route('/finalizar_pedido')
def finalizar_pedido():
    resumo = sistema.finalizar_pedido()
    if resumo:
        cliente = ClienteModel.query.filter_by(cpf=resumo['cliente'].split(",")[1].split(":")[1].strip()).first()
        nova_venda = VendaModel(cliente_id=cliente.id, total=float(resumo['total'][2:]), data_hora=datetime.utcnow())
        db.session.add(nova_venda)
        db.session.commit()
    return jsonify(resumo)

@app.route('/historico_vendas')
def historico_vendas():
    vendas = VendaModel.query.all()
    return render_template('historico_vendas.html', vendas=vendas)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
