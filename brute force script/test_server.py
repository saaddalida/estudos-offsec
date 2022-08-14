from crypt import methods
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
	post_payload = request.form
	username = post_payload.get('username')
	password = post_payload.get('password')
	if username == 'Dalida' and password == '123456':
		return jsonify({'message': 'Login Successful', 'success': True})
	return jsonify({'message': 'Login failed', 'success': False})

app.run()