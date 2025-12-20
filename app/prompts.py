def build_prompt(text: str) -> str:
    return f"""
    You are a helpful AI assistant.

    TASK:
    Summarize the following text in 3 bullet points.

    TEXT:
    {text}

    RULES:
    - Be concise
    - Use clear language
    - Do not invent information
    """
