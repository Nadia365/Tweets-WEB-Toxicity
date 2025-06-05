from dataclasses import dataclass

@dataclass
class Post:
    content: str
    platform: str
    toxicity: float = 0.0
