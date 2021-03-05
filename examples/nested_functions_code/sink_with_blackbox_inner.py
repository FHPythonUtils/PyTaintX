import subprocess

# This is a lib we can't possibly see inside of
import scrypt
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/menu', methods=['POST'])
def menu():
	req_param = request.form['suggestion']

	subprocess.call(scrypt.encypt(scrypt.encypt(req_param)), shell=True)

	with open('menu.txt', 'r', encoding="utf-8") as f:
		menu = f.read()

	return render_template('command_injection.html', menu=menu)
