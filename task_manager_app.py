from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Sample data (can be replaced with a database)
todos = [
    {"id": 1, "task": "Learn Python", "done": False},
    {"id": 2, "task": "Build a web app", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos/<int:task_id>', methods=['GET'])
def get_todo(task_id):
    todo = next((todo for todo in todos if todo['id'] == task_id), None)
    if todo:
        return jsonify(todo)
    else:
        return jsonify({"message": "Task not found"}), 404

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if 'task' in data:
        new_todo = {
            'id': len(todos) + 1,
            'task': data['task'],
            'done': False
        }
        todos.append(new_todo)
        return jsonify(new_todo), 201
    else:
        return jsonify({"message": "Task not provided"}), 400

@app.route('/todos', methods=['PUT'])
def update_multiple_todos():
    data = request.get_json()
    for todo in todos:
        if todo['id'] in data:
            updated_todo = data[todo['id']]
            todo['task'] = updated_todo.get('task', todo['task'])
            todo['done'] = updated_todo.get('done', todo['done'])
    return jsonify(todos)

@app.route('/todos/<int:task_id>', methods=['PUT'])
def update_todo(task_id):
    todo = next((todo for todo in todos if todo['id'] == task_id), None)
    if not todo:
        return jsonify({"message": "Task not found"}), 404

    data = request.get_json()
    if 'task' in data:
        todo['task'] = data['task']
    if 'done' in data:
        todo['done'] = data['done']

    return jsonify(todo)

@app.route('/todos', methods=['DELETE'])
def delete_multiple_todos():
    data = request.get_json()
    task_ids_to_delete = data.get('ids', [])
    global todos
    todos = [todo for todo in todos if todo['id'] not in task_ids_to_delete]
    return jsonify({"message": "Tasks deleted"}), 200

@app.route('/todos/<int:task_id>', methods=['DELETE'])
def delete_todo(task_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != task_id]
    return jsonify({"message": "Task deleted"}), 200

@app.route('/todos/<int:task_id>/due-date', methods=['PUT'])
def add_due_date_to_task(task_id):
    todo = next((todo for todo in todos if todo['id'] == task_id), None)
    if not todo:
        return jsonify({"message": "Task not found"}), 404

    data = request.get_json()
    due_date_str = data.get('due_date')
    try:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"message": "Invalid due date format. Use 'YYYY-MM-DD'"}), 400

    todo['due_date'] = due_date
    return jsonify(todo)

@app.route('/todos/due-date/<string:due_date>', methods=['GET'])
def get_todos_by_due_date(due_date):
    try:
        due_date_obj = datetime.strptime(due_date, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"message": "Invalid due date format. Use 'YYYY-MM-DD'"}), 400

    filtered_todos = [todo for todo in todos if todo.get('due_date') == due_date_obj]
    return jsonify(filtered_todos)

@app.route('/todos/sort-by-due-date', methods=['GET'])
def sort_todos_by_due_date():
    sorted_todos = sorted(todos, key=lambda todo: todo.get('due_date', datetime.max))
    return jsonify(sorted_todos)

if __name__ == '__main__':
    app.run(debug=True)
