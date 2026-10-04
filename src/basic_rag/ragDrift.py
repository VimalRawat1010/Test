try:
    from .cli import main
    from .evaluator import evaluate_faithfulness
    from .models import ClaimVerification
except ImportError:  # pragma: no cover - fallback for direct script execution
    from basic_rag.cli import main
    from basic_rag.evaluator import evaluate_faithfulness
    from basic_rag.models import ClaimVerification


if __name__ == "__main__":
    main()