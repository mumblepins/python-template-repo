# -*- coding: utf-8 -*-
import shutil
import sys

import pytest

if sys.version_info >= (3, 9):
    from importlib.resources import files
else:
    from importlib_resources import files


@pytest.fixture
def temp_path_filled(tmp_path):
    print(tmp_path)

    shutil.copytree(files("tests") / "resources", tmp_path / "src", dirs_exist_ok=True)
    return tmp_path / "src", tmp_path / "dst"
