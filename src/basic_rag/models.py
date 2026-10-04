from pydantic import BaseModel, Field


class ClaimVerification(BaseModel):
    claims: list[str] = Field(description="Atomic claims extracted from the answer")
    faithfulness_score: float = Field(
        description="Fraction of claims supported by context (0.0 to 1.0)"
    )
    unsupported_claims: list[str] = Field(
        description="List of claims not supported by context"
    )
