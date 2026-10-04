from .client import get_openai_client
from .config import get_settings
from .models import ClaimVerification


def build_faithfulness_prompt(context: str, answer: str) -> str:
    return f"""
    Context:
    {context}

    Generated Answer:
    {answer}

    Tasks:
    1. Break down the Generated Answer into atomic claims.
    2. Check each claim against the Context.
    3. Calculate the faithfulness_score = (supported claims / total claims).
    4. List any unsupported claims.
    """


def evaluate_faithfulness(context: str, answer: str, model: str | None = None) -> ClaimVerification:
    client = get_openai_client()
    prompt = build_faithfulness_prompt(context, answer)
    response = client.beta.chat.completions.parse(
        model=model or get_settings().model,
        response_format=ClaimVerification,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.parsed
