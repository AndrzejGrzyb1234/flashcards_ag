import logging

from flashcards.example import add
from flashcards.logging_config import configure_logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Entry point for the flashcards application."""
    configure_logging()
    logger.debug("Application started")

if __name__ == "__main__":
    main()
    add(1, 2)


