from domain.repositories import UserRepository, PostRepository, CommentRepository
from domain.models import User, Post, Comment

class CreateUserUseCase:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, name: str) -> User:
        user = User(id=None, name=name)
        self.user_repo.add_user(user)
        return user

class CreatePostUseCase:
    def __init__(self, post_repo: PostRepository):
        self.post_repo = post_repo

    def execute(self, title: str, content: str, user_id: int) -> Post:
        post = Post(id=None, title=title, content=content, user_id=user_id)
        self.post_repo.add_post(post)
        return post

class GetPostsByUserUseCase:
    def __init__(self, post_repo: PostRepository):
        self.post_repo = post_repo

    def execute(self, user_id: int) -> list[Post]:
        return self.post_repo.get_posts_by_user(user_id)

class AddCommentToPostUseCase:
    def __init__(self, comment_repo: CommentRepository):
        self.comment_repo = comment_repo

    def execute(self, text: str, post_id: int, user_id: int) -> Comment:
        comment = Comment(id=None, text=text, post_id=post_id, user_id=user_id)
        self.comment_repo.add_comment(comment)
        return comment

class GetCommentsForPostUseCase:
    def __init__(self, comment_repo: CommentRepository):
        self.comment_repo = comment_repo

    def execute(self, post_id: int) -> list[Comment]:
        return self.comment_repo.get_comments_by_post(post_id)