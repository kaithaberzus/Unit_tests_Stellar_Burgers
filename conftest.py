from unittest.mock import Mock
import pytest


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'black bun'
    mock_bun.get_price.return_value = 100.0

    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = 'hot sauce'
    mock_ingredient.get_price.return_value = 50.0
    mock_ingredient.get_type.return_value = 'SAUCE'

    return mock_ingredient