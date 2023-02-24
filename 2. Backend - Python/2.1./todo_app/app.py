import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        user='postgres',
        password='coderslab',
        database='todo_app_db'
    )
    return conn

@app.route('/lists', methods = ['GET'])
def get_lists():
    conn = get_db_connection()
    conn.autocommit = True
    c = conn.cursor()
    items = []
    c.execute('Select * from task_list')
    for row in c:
        row = {'id': row[0], 'name': row[1]}
        items.append(row)
    return jsonify(items)

@app.route('/lists', methods = ['POST'])
def create_list():
    new_list = request.get_json()
    title = new_list["title"]
    conn = get_db_connection()
    conn.autocommit = True
    c = conn.cursor()
    query = """insert into task_list(name) values('{title}');"""
    c.execute(query.format(title=title))
    return 'New list item created'

@app.route('/lists/<int:id>', methods=['GET'])
def get_list(id):
    conn = get_db_connection()
    conn.autocommit = True
    c = conn.cursor()
    c.execute("""Select * from task_list where id='{id}';""".format(id=id))
    item = c.fetchone()
    item = {'id': item[0], 'name': item[1]}
    return jsonify(item)

@app.route('/lists/<int:id>', methods=['PUT'])
def update_list(id):
    update_data = request.get_json()
    new_title = update_data["title"]
    conn = get_db_connection()
    conn.autocommit = True
    c = conn.cursor()
    c.execute("""Update task_list set name='{title}' where id='{id}';""".format(id=id, title=new_title))
    return 'List item updated'

@app.route('/lists/<int:id>', methods=['DELETE'])
def delete_list(id):
    conn = get_db_connection()
    conn.autocommit = True
    c = conn.cursor()
    c.execute("""Delete from task_list where id='{id}';""".format(id=id))
    return 'List item deleted'

@app.route('/tasks', methods = ['GET'])
def get_tasks():
    conn = get_db_connection()
    conn.autocommit = True
    c = conn.cursor()
    items = []
    c.execute('Select * from task')
    for row in c:
        row = {'id': row[0], 'name': row[1], 'list': row[2]}
        items.append(row)
    print(items)
    return jsonify(items)

@app.route('/tasks', methods = ['POST'])
def create_task():
    new_task = request.get_json()
    name = new_task["name"]
    list_id = new_task["list_id"]
    conn = get_db_connection()
    conn.autocommit = True
    c = conn.cursor()
    query = """insert into task(name, list_id) values('{name}', '{list_id}');"""
    c.execute(query.format(name=name, list_id=list_id))
    return 'New task created'


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    conn = get_db_connection()
    conn.autocommit = True
    c = conn.cursor()
    c.execute("""Select * from task where id='{id}';""".format(id=id))
    item = c.fetchone()
    item = {'id': item[0], 'name': item[1], 'list': item[2]}
    return jsonify(item)

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    update_data = request.get_json()
    new_name = update_data["name"]
    new_list = update_data["list_id"]
    conn = get_db_connection()
    conn.autocommit = True
    c = conn.cursor()
    c.execute("""Update task set name='{title}', list_id={list_id} where id='{id}';""".format(id=id, title=new_name, list_id=new_list))
    return 'Task item updated'

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = get_db_connection()
    conn.autocommit = True
    c = conn.cursor()
    c.execute("""Delete from task where id='{id}';""".format(id=id))
    return 'Task item deleted'


if __name__ == '__main__':
    app.run(debug=True)