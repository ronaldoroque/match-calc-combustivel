import os
import sys
from typing import Generator

from fastapi.testclient import TestClient
from asyncio import run as aiorun
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_PATH = BASE_DIR + "/src"
sys.path.append(APP_PATH)
os.chdir(APP_PATH)

os.environ['TEST'] = "true"

from src.config import Settings, get_settings
from src.index import app


@pytest.fixture(scope="session")
def client() -> Generator:
    with TestClient(app, base_url="http://localhost:8000") as c:
        yield c


@pytest.fixture(scope="session")
def settings() -> Settings:
    return get_settings()


