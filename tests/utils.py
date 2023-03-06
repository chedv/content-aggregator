import json
import os
import pathlib
from functools import lru_cache
from typing import Any


@lru_cache
def get_path_to_mock_data() -> pathlib.Path:
    return pathlib.Path(os.path.abspath(__file__)).parent / "mock_data"


def load_json(file_name: str) -> Any:
    with open(get_path_to_mock_data() / file_name) as f:
        json_data = json.load(f)
    return json_data
