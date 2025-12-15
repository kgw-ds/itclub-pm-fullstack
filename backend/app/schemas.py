from dataclasses import dataclass

@dataclass(frozen=True)
class PostCreate:
    title: str
    content: str
