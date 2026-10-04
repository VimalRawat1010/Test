from .evaluator_faithfulness import evaluate_faithfulness
from .evaluator_relevance import evaluate_answer_relevance
from .pdf_reader import load_pdf_text


def main() -> None:
    from pathlib import Path
    pdf_path = Path(__file__).resolve().parents[2] / "data" / "Owners_Manual.pdf"
    context_text = load_pdf_text(pdf_path)
    
    answer_text = "The   maximum capacity of frunt trunck is 50Kg. The maximum speed of car is 500Km/h. The car can be driven in snow and rain."

    result = evaluate_faithfulness(context_text, answer_text)
    print(f"Claims: {answer_text}")
    print(f"Faithfulness Score: {result.faithfulness_score}")
    print(f"Unsupported Claims: {result.unsupported_claims}")

    relevance_score = evaluate_answer_relevance(
        query="What is the maximum capacity of frunt trunck ?",
        answer=answer_text
    )
    print(f"Answer Relevance Score (FRUNK): {relevance_score:.4f}")

if __name__ == "__main__":
    main()
