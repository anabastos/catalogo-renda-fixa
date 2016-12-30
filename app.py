from flask import Flask, render_template, jsonify
from pymongo import MongoClient
import requests, json

app = Flask(__name__, static_url_path='/static')

client = MongoClient('localhost:27017')
db = client.teste_db
# app.config['MONGO_DBNAME'] = 'test_db'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/db'

# mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def mostrarContatos():
	# db.catalogo.drop()

	catalogo = get_records();
	if (catalogo.count == 0):
			db.catalogo.insert_many([
				{'nome': 'Lucas', 'email': 'lucas@gmail.com', 'telefone': '11 99389-3244'},
				{'nome': 'Lara', 'email': 'lara@gmail.com', 'telefone': '11 99333-3556'}
			])
	
	return render_template('index.html', catalogo=catalogo)

@app.route('/get_records', methods=['GET'])
def get_records():
	try:
		catalogo_db = db.catalogo.find()
		output = []
		for pessoa in catalogo_db:
			output.append({
					'nome': pessoa['nome'],
					'email': pessoa['email'],
					'telefone': pessoa['telefone']
			})
	except Exception, e:
		return jsonify(status='error', message=str(e))
	return json.dumps(output)

@app.route('/add_record', methods=['POST'])
def add_record():
	try:
		nome = 'nome'
		email = 'email'
		telefone = 'telefone'
		pessoa_id = db.catalogo.insert_one({
			'nome': nome, 'email': email, 'telefone': telefone
			})
		return jsonify(status='ok', message='Inserido corretamente')
	except Exception, e:
		return jsonify(status='error', message=str(e))

if __name__ == "__main__":
	app.run(host= '0.0.0.0', debug=True)
