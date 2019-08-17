import sqlite3

from flask import Flask  # 클래스
from flask import g  # 함수
from flask import render_template  # 함수
from flask import request
from flask import Response

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('test_sqlite.db')  # db가 없을 경dn g의 db를 돌려준다
    return db


@app.teardown_appcontext  # 함수를 읽어서 db를 쓸때 connection을한 후 추 후에 close를 해준다
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/employee', methods=['POST', 'PUT', 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None):
    db = get_db()
    curs = db.cursor()
    curs.execute(
        'CREATE TABLE IF NOT EXISTS person( id '
        'INTEGER PRIMARY KEY AUTOINCREMENT name STRING)'
    )
    name = request.values.get('name', name)
    if request.method == 'GET':
        curs.execute('SELECT * FROM person WHERE name = "{}"'.format(name))
        person = curs.fetchone()
        if not person:
            return "No", 404
        user_id, name = person
        return "{}:{}".format(user_id, name), 200
    if request.method == 'POST':
        curs.execute('INSERT INTO person(name) values("{}")'.format(name))
        db.commit()
        return 'create {}'.format(name), 201
    if request.method == 'PUT':  # updae, 갱신
        new_name = request.values['new_name']  # get일경우 None이 리턴 될 수 있어서 이렇게 에러가 나도록 코드작성함
        curs.execute('UPDATE persons set name = "{}" WHERE name = "{}"'.format(new_name, name))
        db.commit()
        return 'update {} : {}'.format(name, new_name), 200

    if request.method == 'DELETE':
        curs.execute('DELETE from persons WHERE name = "{}"'.format(name))
        db.commit()
        return 'delete {}'.format(name), 200

    curs.close()


@app.route('/')  # web에 /가 오면 바로 해당 반환 내용을 반환 해 달라는 뜻
def hello_world():
    return 'top'


@app.route('/hello')
@app.route('/hello/<username>')
def hello_word2(username=None):
    return 'hello word! {}'.format(username)
    # return render_template('hello.html', username=username)


@app.route('/post', methods=['POST', 'PUT', 'DELETE'])
def show_post():
    return str(request.values)


def main():
    app.debug = True
    # app.run() 밑에 것과 default가 동일
    app.run(host="127.0.0.1", port=5000)


if __name__ == '__main__':
    main()
