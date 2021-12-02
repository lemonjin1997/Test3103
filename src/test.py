import pytest
from app import check_content

class TestUtil:
    def test_check_content(self):
        assert check_content("<h1>lol</h1>") == False, "Test failed"
