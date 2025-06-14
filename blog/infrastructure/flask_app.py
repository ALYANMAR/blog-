from flask import Flask, request, jsonify
from application.use_cases import *
from application.factories import RepositoryFactory

app = Flask(__name__)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    repo = RepositoryFactory.create_user_repository()
    use_case = CreateUserUseCase(repo)
    user = use_case.execute(data["name"])
    return jsonify({"id": user.id, "name": user.name}), 201

@app.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    repo = RepositoryFactory.create_post_repository()
    use_case = CreatePostUseCase(repo)
    post = use_case.execute(data["title"], data["content"], data["user_id"])
    return jsonify({"id": post.id, "title": post.title, "user_id": post.user_id}), 201

@app.route("/posts/<int:user_id>", methods=["GET"])
def get_posts_by_user(user_id):
    post_repo = RepositoryFactory.create_post_repository()
    use_case = GetPostsByUserUseCase(post_repo)
    posts = use_case.execute(user_id)
    return jsonify([{"id": p.id, "title": p.title} for p in posts])

@app.route("/comments", methods=["POST"])
def add_comment():
    data = request.json
    repo = RepositoryFactory.create_comment_repository()
    use_case = AddCommentToPostUseCase(repo)
    comment = use_case.execute(data["text"], data["post_id"], data["user_id"])
    return jsonify({"id": comment.id, "text": comment.text}), 201

@app.route("/comments/<int:post_id>", methods=["GET"])
def get_comments_for_post(post_id):
    repo = RepositoryFactory.create_comment_repository()
    use_case = GetCommentsForPostUseCase(repo)
    comments = use_case.execute(post_id)
    return jsonify([{"id": c.id, "text": c.text, "user_id": c.user_id} for c in comments])

if __name__ == "__main__":
    app.run(debug=True)