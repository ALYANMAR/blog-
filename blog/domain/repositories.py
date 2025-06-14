from abc import ABC, abstractmethod
from domain.models import User, Post, Comment
from typing import Optional

class UserRepository(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def add_user(self, user: User) -> None:
        pass

class PostRepository(ABC):
    @abstractmethod
    def get_post_by_id(self, post_id: int) -> Optional[Post]:
        pass

    @abstractmethod
    def add_post(self, post: Post) -> None:
        pass

    @abstractmethod
    def get_posts_by_user(self, user_id: int) -> list[Post]:
        pass

class CommentRepository(ABC):
    @abstractmethod
    def get_comments_by_post(self, post_id: int) -> list[Comment]:
        pass

    @abstractmethod
    def add_comment(self, comment: Comment) -> None:
        pass