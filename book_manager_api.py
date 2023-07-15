from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (can be replaced with a database)
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
]

# Route to get all books (GET request)
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Route to get a specific book by ID (GET request)
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"message": "Book not found"}), 404

# Route to create a new book (POST request)
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if 'title' in data and 'author' in data:
        new_book = {
            'id': len(books) + 1,
            'title': data['title'],
            'author': data['author']
        }
        books.append(new_book)
        return jsonify(new_book), 201
    else:
        return jsonify({"message": "Title and author are required"}), 400

# Route to update an existing book (PUT request)
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if not book:
        return jsonify({"message": "Book not found"}), 404

    data = request.get_json()
    if 'title' in data:
        book['title'] = data['title']
    if 'author' in data:
        book['author'] = data['author']

    return jsonify(book)

# Route to delete a book (DELETE request)
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({"message": "Book deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
