from typing import List


def build_itinerary(places: List[str], days: int) -> str:
    """
    Build a day-by-day itinerary by distributing places across travel days.

    Args:
        places: List of places to visit.
        days: Number of travel days.

    Returns:
        A formatted itinerary string.

    Raises:
        ValueError: If days is less than 1 or places is empty.
    """
    if days < 1:
        raise ValueError("Days must be at least 1.")
    if not places:
        raise ValueError("Places list must not be empty.")

    itinerary_lines: List[str] = []
    total_places = len(places)
    per_day = max(1, total_places // days)
    extra = total_places % days

    index = 0
    for day in range(1, days + 1):
        count_for_day = per_day + (1 if extra > 0 else 0)
        if extra > 0:
            extra -= 1

        selected_places = places[index:index + count_for_day]
        index += count_for_day

        if not selected_places:
            itinerary_lines.append(
                f"Day {day}: Morning - Free time, Afternoon - Explore local area, Evening - Rest"
            )
            continue

        morning = selected_places[0]
        afternoon = (
            selected_places[1] if len(selected_places) > 1 else "Local food experience"
        )
        evening = (
            selected_places[2] if len(selected_places) > 2 else "Relax and explore town"
        )

        itinerary_lines.append(
            f"Day {day}: Morning - {morning}, Afternoon - {afternoon}, Evening - {evening}"
        )

    return "\n".join(itinerary_lines)