from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: Optional[int]
    name: str

@dataclass
class Post:
    id: Optional[int]
    title: str
    content: str
    user_id: int

@dataclass
class Comment:
    id: Optional[int]
    text: str
    post_id: int
    user_id: int