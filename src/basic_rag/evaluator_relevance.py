import numpy as np
from .client import get_openai_client
from .config import get_settings
from .models import ClaimVerification


def get_embedding(text: str) -> np.ndarray:
    client = get_openai_client()
    res = client.embeddings.create(input=text, model="text-embedding-3-small")
    return np.array(res.data[0].embedding)

def evaluate_answer_relevance(query: str, answer: str, num_gen_questions: int = 3) -> float:
    # 1. Reverse-generate questions that the answer would address
    prompt = f"Generate {num_gen_questions} hypothetical user questions that this answer directly addresses:\nAnswer: {answer}"
    client = get_openai_client()
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    generated_questions = res.choices[0].message.content.strip().split("\n")
    
    # 2. Compute similarity between original query and generated questions
    query_emb = get_embedding(query)
    similarities = []
    
    for q in generated_questions:
        q_emb = get_embedding(q)
        sim = np.dot(query_emb, q_emb) / (np.linalg.norm(query_emb) * np.linalg.norm(q_emb))
        similarities.append(sim)
        
    return float(np.mean(similarities))

score = evaluate_answer_relevance(
    query="What is the charging capacity of the vehicle?",
    answer="The vehicle supports DC fast charging up to 250 kW."
)
#print(f"Answer Relevance Score is : {score:.4f}")