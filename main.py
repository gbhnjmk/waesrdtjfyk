
from flask import Flask, render_template, request, make_response, jsonify, url_for

from flask import make_response
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    return render_template('main.html')


@app.route("/about")
def about():
    return render_template('main.html')


@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/admin_add")
def adminka():
    return render_template('admin.html')


""""@app.route('/items/<int:id>', methods=['GET', 'POST'])
def show_item(id):
    return render_template('view_item.html', title='About a product', item=item)"""


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Permission denied'}), 404)


@app.after_request
def add_header(response):
    response.cache_control.max_age = 0
    return response


def main():
    app.run()


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
