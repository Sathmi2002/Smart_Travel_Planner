def clean_agent_output(text: str, fallback: str) -> str:
    """
    Clean problematic LLM responses. If the output contains refusal-style text,
    return the trusted fallback instead.

    Args:
        text: Raw LLM output.
        fallback: Safe fallback text from tool/state data.

    Returns:
        Cleaned output string.
    """
    if not text:
        return fallback

    lowered = text.lower()

    refusal_patterns = [
        "i can't help",
        "i cannot help",
        "i can't assist",
        "i cannot assist",
        "i am not able to provide",
        "missing information",
        "incomplete information",
        "do not have enough information",
        "cannot provide recommendations",
    ]

    for pattern in refusal_patterns:
        if pattern in lowered:
            return fallback

    return text.strip()