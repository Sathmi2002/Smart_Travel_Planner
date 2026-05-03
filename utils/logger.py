import logging
import os


def setup_logger() -> logging.Logger:
    """Configure and return the application logger."""
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("travel_planner")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler("logs/run.log", encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger