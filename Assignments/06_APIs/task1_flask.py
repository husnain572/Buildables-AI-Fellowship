from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    todos.append({'task': data['task']})
    return jsonify({'message': 'Task added successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
