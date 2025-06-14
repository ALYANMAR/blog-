import sqlite3
from domain.models import User, Post, Comment
from domain.repositories import UserRepository, PostRepository, CommentRepository
from typing import Optional

class SQLiteUserRepository(UserRepository):
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        with sqlite3.connect("blog.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name FROM users WHERE id=?", (user_id,))
            row = cursor.fetchone()
            if row:
                return User(id=row[0], name=row[1])
            return None

    def add_user(self, user: User) -> None:
        with sqlite3.connect("blog.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name) VALUES (?)", (user.name,))
            user.id = cursor.lastrowid

class SQLitePostRepository(PostRepository):
    def get_post_by_id(self, post_id: int) -> Optional[Post]:
        with sqlite3.connect("blog.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, content, user_id FROM posts WHERE id=?", (post_id,))
            row = cursor.fetchone()
            if row:
                return Post(id=row[0], title=row[1], content=row[2], user_id=row[3])
            return None

    def add_post(self, post: Post) -> None:
        with sqlite3.connect("blog.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)",
                           (post.title, post.content, post.user_id))
            post.id = cursor.lastrowid

    def get_posts_by_user(self, user_id: int) -> list[Post]:
        with sqlite3.connect("blog.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, content, user_id FROM posts WHERE user_id=?", (user_id,))
            rows = cursor.fetchall()
            return [Post(id=r[0], title=r[1], content=r[2], user_id=r[3]) for r in rows]

class SQLiteCommentRepository(CommentRepository):
    def get_comments_by_post(self, post_id: int) -> list[Comment]:
        with sqlite3.connect("blog.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, text, post_id, user_id FROM comments WHERE post_id=?", (post_id,))
            rows = cursor.fetchall()
            return [Comment(id=r[0], text=r[1], post_id=r[2], user_id=r[3]) for r in rows]

    def add_comment(self, comment: Comment) -> None:
        with sqlite3.connect("blog.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO comments (text, post_id, user_id) VALUES (?, ?, ?)",
                           (comment.text, comment.post_id, comment.user_id))
            comment.id = cursor.lastrowid