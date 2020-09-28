from bottle import route, run, static_file


@route('/')
def home():
    return static_file('index.html', root='.')


run(host='0.0.0.0', port=80)
