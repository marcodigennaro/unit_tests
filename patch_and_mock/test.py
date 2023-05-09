from unittest.mock import patch
from main import parse


@patch('main.fetch_net')
def test_parse_from_fetch_net(mock_get):
    mock_get.return_value = "def"
    assert parse() == 'status = def'



