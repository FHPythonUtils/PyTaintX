import subprocess

# This is a lib we can't possibly see inside of
import scrypt
from flask import Flask, render_template, request

app = Flask(__name__)


def inner(inner_arg):
	yes_vuln = inner_arg + 'hey'
	return yes_vuln


@app.route('/menu', methods=['POST'])
def menu():
	req_param = request.form['suggestion']

	# blackbox(user_defined_inner())
	foo = scrypt.encrypt(inner(req_param))
	subprocess.call(foo, shell=True)

	with open('menu.txt', 'r', encoding="utf-8") as f:
		menu = f.read()

	return render_template('command_injection.html', menu=menu)
