import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, MagicMock, patch
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.model import FileModel, FileInfo


class TestGUIControllerLogic:
    @pytest.fixture
    def temp_dir(self):
        temp = tempfile.mkdtemp()
        yield Path(temp)
        shutil.rmtree(temp)

    @pytest.fixture
    def controller_mock(self, temp_dir):
        (temp_dir / "file1.txt").write_text("content1")
        (temp_dir / "file2.txt").write_text("content2")
        (temp_dir / "file3.txt").write_text("content1")
        (temp_dir / "file4.txt").write_text("content4")

        with patch("app.gui.FileSelector") as MockGui:
            mock_gui = Mock()
            mock_gui.file_listbox = Mock()
            mock_gui.delete_entry = Mock()
            mock_gui.log_text = Mock()
            mock_gui.folder_label = Mock()
            mock_gui.show_info = Mock()
            mock_gui.show_error = Mock()
            mock_gui.show_confirm = Mock(return_value=True)
            mock_gui.display_files = Mock()
            mock_gui.display_by_extension = Mock()
            mock_gui.log_message = Mock()
            mock_gui.set_selection_label = Mock()
            mock_gui.clear_selection_label = Mock()
            mock_gui.clear_exceptions = Mock()
            mock_gui.get_exceptions = Mock(return_value=[])

            MockGui.return_value = mock_gui

            from app.gui_controller import GUIController

            controller = GUIController()

            return controller

    def test_set_directory_valid(self, controller_mock, temp_dir):
        result = controller_mock.set_directory(str(temp_dir))
        assert result is True
        assert controller_mock.model is not None

    def test_set_directory_invalid(self, controller_mock):
        result = controller_mock.set_directory("C:/invalid/path")
        assert result is False

    def test_on_select_folder(self, controller_mock, temp_dir):
        controller_mock.set_directory(str(temp_dir))
        controller_mock.on_select_folder()

        assert len(controller_mock.current_files) == 4
        controller_mock.gui.display_files.assert_called()
        controller_mock.gui.log_message.assert_called()

    def test_on_classify_no_model(self, controller_mock):
        controller_mock.model = None
        controller_mock.gui.show_error = Mock()

        controller_mock.on_classify()

        controller_mock.gui.show_error.assert_called()

    def test_on_show_all_no_files(self, controller_mock):
        controller_mock.current_files = []
        controller_mock.gui.show_error = Mock()

        controller_mock.on_show_all()

        controller_mock.gui.show_error.assert_called()

    def test_on_exceptions_no_model(self, controller_mock):
        controller_mock.gui.show_exclusion_dialog = Mock(return_value=["file1.txt"])

        controller_mock.on_exceptions()

        controller_mock.gui.set_exceptions.assert_called()

    def test_on_exceptions_with_dialog(self, controller_mock):
        controller_mock.gui.show_exclusion_dialog = Mock(
            return_value=["file1.txt", "file2.txt"]
        )

        controller_mock.on_exceptions()

        controller_mock.gui.set_exceptions.assert_called_with(
            ["file1.txt", "file2.txt"]
        )
        controller_mock.gui.log_message.assert_called()

    def test_on_delete_selection_no_files(self, controller_mock):
        controller_mock.model = None
        controller_mock.gui.show_warning = Mock()

        controller_mock.on_delete_selection()

        controller_mock.gui.show_warning.assert_called()

    def test_on_delete_selection_no_selection(self, controller_mock, temp_dir):
        controller_mock.set_directory(str(temp_dir))
        controller_mock.on_select_folder()
        controller_mock.gui.open_file_selection = Mock(return_value=[])

        controller_mock.on_delete_selection()

        controller_mock.gui.log_message.assert_called()


class TestFileSelectorViewLogic:
    def test_format_size_bytes(self):
        from app.gui import FileSelector

        with patch("tkinter.Tk"):
            gui = FileSelector()
            assert gui._format_size(500) == "500.0 B"

    def test_format_size_kilobytes(self):
        from app.gui import FileSelector

        with patch("tkinter.Tk"):
            gui = FileSelector()
            assert gui._format_size(2048) == "2.0 KB"

    def test_format_size_megabytes(self):
        from app.gui import FileSelector

        with patch("tkinter.Tk"):
            gui = FileSelector()
            assert gui._format_size(2097152) == "2.0 MB"


class TestGUIInteractions:
    @pytest.fixture
    def temp_dir(self):
        temp = tempfile.mkdtemp()
        yield Path(temp)
        shutil.rmtree(temp)

    def test_exclusion_dialog_mock(self, temp_dir):
        mock_parent = Mock()
        mock_parent.transient = Mock()
        mock_parent.grab_set = Mock()

        from app.gui import ExclusionDialog

        assert ExclusionDialog is not None
