from src.main import main
import pytest
from unittest.mock import Mock

class TestMain:
    @pytest.mark.it('test generate search file is called with no input')
    def test_main_generate_search(self,monkeypatch):
        mock = Mock()
        inputs=iter(["s", "x"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        monkeypatch.setattr("src.main.generate_search_file", mock)
        with pytest.raises(SystemExit):
            main()

        mock.assert_called_once()
    
    @pytest.mark.it('test generate search file is called with advanced')
    def test_main_advanced_search(self, monkeypatch):
        mock = Mock()
        inputs=iter(["A", "x"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        monkeypatch.setattr("src.main.generate_search_file", mock)
        with pytest.raises(SystemExit):
            main()

        mock.assert_called_with(advanced=True)

    @pytest.mark.it(' perform search is called with default')
    def test_main_default_search(self,monkeypatch):
        mock = Mock()
        inputs=iter(["D", "x"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        monkeypatch.setattr("src.main.perform_search", mock)
        with pytest.raises(SystemExit):
            main()
        mock.assert_called_once()

    @pytest.mark.it('list search directory is called properly and args passed to perform')
    def test_main_List_directory(self, monkeypatch):
        test_dict={"search_directory":"test_search_directory", "filename":"Test_fileName"}
        mock = Mock(side_effect=lambda :test_dict)
        mock2=Mock()
        inputs=iter(["L", "x"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        monkeypatch.setattr("src.main.list_search_directory", mock)
        monkeypatch.setattr("src.main.perform_search", mock2)
        with pytest.raises(SystemExit):
            main()
        mock.assert_called_once()
        mock2.assert_called_with(search_directory="test_search_directory", search_filename="Test_fileName")

    @pytest.mark.it('manual search is called with default')
    def test_main_manual_search(self, monkeypatch):
        mock = Mock()
        inputs=iter(["M", "x"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        monkeypatch.setattr("src.main.manual_search", mock)
        with pytest.raises(SystemExit):
            main()
        mock.assert_called_once()