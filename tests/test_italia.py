from unittest.mock import patch


def test_open_webbrowser():
    with patch("webbrowser.open") as mock_open:
        import italia  # noqa

        mock_open.assert_called_once_with("https://pycon.it")
