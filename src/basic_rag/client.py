from openai import OpenAI
from .config import get_settings


def get_openai_client(api_key: str | None = None) -> OpenAI:
    resolved_key = api_key or get_settings().openai_api_key
    if not resolved_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Export it before running evaluate_faithfulness(): "
            "export OPENAI_API_KEY='your-key-here'"
        )
    return OpenAI(api_key=resolved_key)
