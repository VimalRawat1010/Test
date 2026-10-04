from .evaluator import evaluate_faithfulness
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


if __name__ == "__main__":
    main()
