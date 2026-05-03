from typing import Dict, List


DESTINATION_PLACES: Dict[str, List[str]] = {
    "ella": [
        "Nine Arch Bridge",
        "Little Adam's Peak",
        "Ella Rock",
        "Ravana Falls",
        "Halpewatte Tea Factory",
    ],
    "kandy": [
        "Temple of the Tooth",
        "Kandy Lake",
        "Royal Botanical Gardens",
        "Bahirawakanda Temple",
        "Udawatta Kele Sanctuary",
    ],
    "galle": [
        "Galle Fort",
        "Galle Lighthouse",
        "Dutch Reformed Church",
        "Jungle Beach",
        "Maritime Museum",
    ],
    "nuwara eliya": [
        "Gregory Lake",
        "Hakgala Botanical Garden",
        "Pedro Tea Estate",
        "Seetha Amman Temple",
        "Victoria Park",
    ],
    "sigiriya": [
        "Sigiriya Rock Fortress",
        "Pidurangala Rock",
        "Sigiriya Museum",
        "Village Tour",
        "Minneriya National Park",
    ],
    "kurunegala": [
        "Ethagala (Elephant Rock)",
        "Ridi Viharaya",
        "Panduwasnuwara Kingdom",
        "Kurunegala Lake",
        "Athugala Temple",
    ],
    "yala": [
        "Yala National Park",
        "Safari Jeep Tour",
        "Tissamaharama Lake",
        "Kirinda Beach",
        "Sithulpawwa Temple",
    ],
}


def get_places(destination: str) -> List[str]:
    """
    Return a list of known attractions for the given destination.

    Args:
        destination: Name of the destination.

    Returns:
        A list of attractions.

    Raises:
        ValueError: If the destination is empty.
    """
    if not destination or not destination.strip():
        raise ValueError("Destination must not be empty.")

    key = destination.strip().lower()
    return DESTINATION_PLACES.get(
        key,
        [
            "Main town area",
            "Popular viewpoint",
            "Local cultural site",
            "Food street",
            "Nature attraction",
        ],
    )