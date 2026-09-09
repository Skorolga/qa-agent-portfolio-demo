from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    base_url: str
    environment: str = "test"

def load_settings() -> Settings:
    return Settings(
        base_url=os.getenv("BASE_URL", "https://example.test"),
        environment=os.getenv("ENV", "test"),
    )
