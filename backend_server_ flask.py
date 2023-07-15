from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (can be replaced with a database)
todos = [
    {"id": 1, "task": "Learn Python", "done": False},
    {"id": 2, "task": "Build a web app", "done": False}
]

# Route to get all tasks (GET request)
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Route to get a specific task (GET request)
@app.route('/todos/<int:task_id>', methods=['GET'])
def get_todo(task_id):
    todo = next((todo for todo in todos if todo['id'] == task_id), None)
    if todo:
        return jsonify(todo)
    else:
        return jsonify({"message": "Task not found"}), 404

# Route to create a new task (POST request)
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

# Route to update an existing task (PUT request)
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

# Route to delete a task (DELETE request)
@app.route('/todos/<int:task_id>', methods=['DELETE'])
def delete_todo(task_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
