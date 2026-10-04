import os
doc= """Agenta is an innovative open-source platform crafted to simplify and accelerate
the entire lifecycle of large language model (LLM) applications. It offers comprehensive
tools that cover every critical phase—from prompt engineering and fine-tuning to rigorous
evaluation and seamless deployment. At its core, Agenta supports version control for
prompts, allowing developers to experiment with and compare multiple prompt variants
side-by-side, thereby identifying the most effective approaches efficiently. Moreover,
it integrates built-in workflows for human feedback and annotation, empowering teams to
iteratively refine prompts and models based on real-world interactions and user input.
Agenta’s deployment features ensure smooth and scalable integration of LLM applications
into production environments, enabling businesses to deliver AI-driven solutions reliably
. To complement this, the platform includes robust observability and monitoring tools
that provide detailed insights into model performance metrics, user behavior, and error
cases—all consolidated into a single, intuitive dashboard. This end-to-end capability
makes Agenta a powerful ally for AI teams looking to build, optimize, and maintain
high-quality language model services with greater agility and transparency."""

def analyze_chunks(chunks, use_tokens=False):
    print("\\nNumber of Chunks:", len(chunks))

    if len(chunks) < 2:
        print("Not enough chunks to analyze overlaps.")
        return

    # Pick the middle pair of chunks (or just the last two if fewer than 200)
    idx1 = max(0, len(chunks) // 2 - 1)
    idx2 = idx1 + 1

    print("\\n", "="*50, f"Chunk {idx1}", "="*50, "\\n", chunks[idx1])
    print("\\n", "="*50, f"Chunk {idx2}", "="*50, "\\n", chunks[idx2])

    chunk1, chunk2 = chunks[idx1], chunks[idx2]

    if use_tokens:
        encoding = tiktoken.get_encoding("cl100k_base")
        tokens1 = encoding.encode(chunk1)
        tokens2 = encoding.encode(chunk2)

        for i in range(len(tokens1), 0, -1):
            if tokens1[-i:] == tokens2[:i]:
                overlap = encoding.decode(tokens1[-i:])
                print("\\nOverlapping text ({} tokens):\\n{}".format(i, overlap))
                return
        print("\\nNo token overlap found.")
    else:
        for i in range(min(len(chunk1), len(chunk2)), 0, -1):
            if chunk1[-i:] == chunk2[:i]:
                print("\\nOverlapping text ({} chars):\\n{}".format(i, chunk1[-i:]))
                return
        print("\\nNo character overlap found.")



        
def chunk_text(document, chunk_size, overlap):
    chunks = []
    stride = chunk_size - overlap
    current_idx = 0

    while current_idx < len(document):
        # Take chunk_size characters starting from current_idx
        chunk = document[current_idx:current_idx + chunk_size]
        if not chunk:  # Break if we're out of text
            break
        chunks.append(chunk)
        current_idx += stride  # Move forward by stride

    return chunks

character_chunks = chunk_text(doc, chunk_size=100, overlap=0)

analyze_chunks(character_chunks)