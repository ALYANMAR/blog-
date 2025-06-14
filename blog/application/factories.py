from infrastructure.repositories import SQLiteUserRepository, SQLitePostRepository, SQLiteCommentRepository

class RepositoryFactory:
    @staticmethod
    def create_user_repository():
        return SQLiteUserRepository()

    @staticmethod
    def create_post_repository():
        return SQLitePostRepository()

    @staticmethod
    def create_comment_repository():
        return SQLiteCommentRepository()