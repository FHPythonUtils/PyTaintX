import random
import string

from flask import Flask, make_response, render_template, request

app = Flask(__name__)


@app.route('/example2')
def example2():
	return render_template('example2_form.html')


html1 = open('templates/example2_response.html', encoding="utf-8").read()


@app.route('/example2action', methods=['POST'])
def example2_action():
	data = request.form['my_text']
	resp = make_response(html1.replace('{{ data }}', data))
	resp.set_cookie(
	'session_id',
	''.join(random.choice(string.ascii_uppercase) for x in range(16)))
	return resp


if __name__ == '__main__':
	app.run(debug=True)
