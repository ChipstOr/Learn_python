from flask import Flask, request, jsonify

app = Flask(__name__)
posts = []

@app.route("/")
def index():
    return "Start page"


@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    post = {
        'id': len(posts) + 1,
        'title': data['title'],
        'content': data['content'],
        'author_id': data['author_id']
    }
    posts.append(post)
    return jsonify(post), 201


@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)


@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    return jsonify(post)


@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    data = request.get_json()
    post['title'] = data['title']
    post['content'] = data['content']
    return jsonify(post)


@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    posts.remove(post)
    return jsonify({'success': 'Post deleted'}), 200


if __name__ == "__main__":
    app.run(debug=True)