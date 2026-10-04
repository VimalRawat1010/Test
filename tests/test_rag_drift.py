import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


def test_module_imports_without_openai_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    module = importlib.import_module("basic_rag.ragDrift")

    assert hasattr(module, "evaluate_faithfulness")
