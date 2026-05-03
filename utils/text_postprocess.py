def remove_duplicate_lines(text: str) -> str:
    """
    Remove duplicate lines while preserving order.
    """
    seen = set()
    result = []

    for line in text.splitlines():
        clean = line.strip()
        if clean and clean not in seen:
            seen.add(clean)
            result.append(line)

    return "\n".join(result)