from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/XSS_param', methods=['GET'])
def XSS1():
	param = request.args.get('param', 'not set')

	other_var = param + ''

	not_the_same_var = '' + other_var

	another_one = not_the_same_var + ''

	html = open('templates/XSS_param.html', encoding="utf-8").read()
	resp = make_response(html.replace('{{ param }}', another_one))

	return resp


if __name__ == '__main__':
	app.run(debug=True)
