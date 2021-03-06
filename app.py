from flask import Flask, render_template, jsonify, request, json
from pymongo import MongoClient


app = Flask(__name__, static_url_path='/static')

client = MongoClient('localhost:27017')
db = client.teste_db

@app.route('/', methods=['GET'])
def mostrarContatos():

	catalogo = get_records();
	if db.catalogo.count(0) == 0:
		db.catalogo.insert_many([
			{'nome': 'Lucas', 'email': 'lucas@gmail.com', 'telefone': '11 99389-3244'},
			{'nome': 'Lara', 'email': 'lara@gmail.com', 'telefone': '11 99333-3556'}
		])
	
	return render_template('index.html', catalogo=catalogo)

@app.route('/get_records', methods=['GET'])
def get_records():
	try:
		catalogo_db = db.catalogo.find()
		catalogo_list = []
		for pessoa in catalogo_db:
			catalogo_list.append({
					'nome': pessoa['nome'],
					'email': pessoa['email'],
					'telefone': pessoa['telefone']
			})
	except Exception, e:
		return jsonify(status='error', message=str(e))
	return json.dumps(catalogo_list)

@app.route('/insert_record', methods=['POST'])
def insert_record():
	try:
		json_data = request.json['form']
		nome = json_data['nome']
		email = json_data['email']
		telefone = json_data['telefone']
		pessoa_id = db.catalogo.insert_one({
			'nome': nome, 'email': email, 'telefone': telefone
			})
		return jsonify(status='ok', message='Inserido corretamente')
	except Exception, e:
		return jsonify(status='error', message=str(e))

if __name__ == "__main__":
	app.run(host= '0.0.0.0', debug=True)
