import logging

from utils import log_around

logger = logging.getLogger(__name__)


# example of use logger, without decorator
# def add(a: int, b: int) -> int:
#     """Add."""
#     logger.debug("Calling %s", add.__qualname__, extra={"a": a, "b": b})
#     result =  a + b
#     logger.debug("Result of addition %s", add.__qualname__, extra={"result": result})
#     return result

@log_around
def add(a: int, b: int) -> int:
    """Add."""
    return a + b
