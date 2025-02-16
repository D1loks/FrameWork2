import pytest
from reportportal_client import RPLogger, RPLogHandler
import logging


@pytest.fixture(scope="session")
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    rp_handler = RPLogHandler()
    rp_handler.setLevel(logging.DEBUG)

    logger.addHandler(rp_handler)
    return logger
