from flask import Flask, request, jsonify, make_response, render_template

app = Flask(__name__)

# 1. Роут для GET-запросов
@app.route('/get-route', methods=['GET'])
def handle_get():
    if request.method == 'GET':
        params = request.args.to_dict()  # Получаем параметры из GET-запроса
        return jsonify(params)           # Возвращаем их в формате JSON
    else:
        return make_response("Method Not Allowed", 405)

# 2. Роут для POST-запросов
@app.route('/post-route', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        params = request.form.to_dict()  # Получаем параметры из POST-запроса
        return jsonify(params)           # Возвращаем их в формате JSON
    else:
        return make_response("Method Not Allowed", 405)

# 3. Роут для HEAD-запросов
@app.route('/head-route', methods=['HEAD'])
def handle_head():
    if request.method == 'HEAD':
        response = make_response('', 200)
        response.headers['Content-Type'] = 'text/plain'
        return response
    else:
        return make_response("Method Not Allowed", 405)

# 4. Роут для OPTIONS-запросов
@app.route('/options-route', methods=['OPTIONS'])
def handle_options():
    if request.method == 'OPTIONS':
        response = make_response('', 204)
        response.headers['Allow'] = 'OPTIONS, GET, POST, HEAD'
        return response
    else:
        return make_response("Method Not Allowed", 405)

# Главная страница с ссылками на все роуты
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
