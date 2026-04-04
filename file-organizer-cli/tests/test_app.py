import pytest
import tempfile
import shutil
from pathlib import Path
from io import StringIO
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.model import FileModel, FileInfo, LogManager
from app.view import View
from app.controller import Controller


class TestModel:
    @pytest.fixture
    def temp_dir(self):
        temp = tempfile.mkdtemp()
        yield Path(temp)
        shutil.rmtree(temp)

    @pytest.fixture
    def sample_files(self, temp_dir):
        files = []
        for i in range(5):
            path = temp_dir / f"file{i}.txt"
            path.write_text(f"content {i}")
            files.append(path)
        return files

    def test_validate_path_exists(self, temp_dir):
        model = FileModel(str(temp_dir))
        assert model.validate_path() is True

    def test_validate_path_not_exists(self):
        model = FileModel("C:/nonexistent/path")
        assert model.validate_path() is False

    def test_scan_files(self, temp_dir, sample_files):
        model = FileModel(str(temp_dir))
        files = model.scan_files()
        assert len(files) == 5

    def test_scan_files_recursive(self, temp_dir):
        subdir = temp_dir / "sub"
        subdir.mkdir()
        (temp_dir / "file1.txt").write_text("1")
        (subdir / "file2.txt").write_text("2")

        model = FileModel(str(temp_dir))

        files = model.scan_files(recursive=False)
        assert len(files) == 1

        files = model.scan_files(recursive=True)
        assert len(files) == 2

    def test_classify_by_extension(self, temp_dir):
        (temp_dir / "doc1.txt").write_text("txt")
        (temp_dir / "doc.pdf").write_text("pdf")
        (temp_dir / "doc2.txt").write_text("txt2")

        model = FileModel(str(temp_dir))
        model.scan_files()
        classified = model.classify_by_extension()

        assert ".txt" in classified
        assert ".pdf" in classified
        assert len(classified[".txt"]) == 2
        assert len(classified[".pdf"]) == 1

    def test_get_file_by_name(self, temp_dir):
        (temp_dir / "test.txt").write_text("content")

        model = FileModel(str(temp_dir))
        model.scan_files()

        found = model.get_file_by_name("test.txt")
        assert found is not None
        assert found.name == "test.txt"

        not_found = model.get_file_by_name("nonexistent.txt")
        assert not_found is None

    def test_get_files_by_names(self, temp_dir):
        (temp_dir / "file1.txt").write_text("1")
        (temp_dir / "file2.txt").write_text("2")
        (temp_dir / "file3.txt").write_text("3")

        model = FileModel(str(temp_dir))
        model.scan_files()

        found, not_found = model.get_files_by_names(["file1.txt", "file4.txt"])

        assert len(found) == 1
        assert len(not_found) == 1
        assert not_found[0] == "file4.txt"

    def test_delete_file(self, temp_dir):
        file_path = temp_dir / "delete_me.txt"
        file_path.write_text("content")

        model = FileModel(str(temp_dir))
        model.scan_files()

        file_info = model.get_file_by_name("delete_me.txt")
        success, message = model.delete_file(file_info)

        assert success is True
        assert file_path.exists() is False

    def test_delete_file_not_exists(self, temp_dir):
        model = FileModel(str(temp_dir))
        model.scan_files()

        fake_file = FileInfo(
            path=temp_dir / "fake.txt", name="fake.txt", extension=".txt", size=0
        )

        success, message = model.delete_file(fake_file)
        assert success is False
        assert "no existe" in message

    def test_calculate_hash(self, temp_dir):
        file1 = temp_dir / "file1.txt"
        file2 = temp_dir / "file2.txt"
        file1.write_text("same content")
        file2.write_text("same content")

        model = FileModel(str(temp_dir))

        hash1 = model.calculate_hash(file1)
        hash2 = model.calculate_hash(file2)

        assert hash1 == hash2

    def test_find_duplicates(self, temp_dir):
        (temp_dir / "dup1.txt").write_text("duplicate")
        (temp_dir / "dup2.txt").write_text("duplicate")
        (temp_dir / "unique.txt").write_text("unique")

        model = FileModel(str(temp_dir))
        model.scan_files()
        duplicates = model.find_duplicates()

        assert len(duplicates) == 1
        assert len(duplicates[0]) == 2


class TestLogManager:
    @pytest.fixture
    def temp_logs(self):
        temp = tempfile.mkdtemp()
        yield Path(temp)
        shutil.rmtree(temp)

    def test_save_file_list(self, temp_logs):
        files = [
            FileInfo(Path("file1.txt"), "file1.txt", ".txt", 100),
            FileInfo(Path("file2.txt"), "file2.txt", ".txt", 200),
        ]

        manager = LogManager(temp_logs)
        filepath = manager.save_archive_list(files, "/test/path")

        assert filepath.exists()
        assert "file1.txt" in filepath.read_text()
        assert "file2.txt" in filepath.read_text()

    def test_append_elimination_log(self, temp_logs):
        manager = LogManager(temp_logs)

        manager.save_elimination_log(
            ["file1.txt", "file2.txt"], [], [], "/test", "test"
        )
        manager.save_elimination_log(["file3.txt"], [], [], "/test", "test")

        filepath = manager.get_elimination_log_path()
        content = filepath.read_text()

        assert "file1.txt" in content
        assert "file2.txt" in content
        assert "file3.txt" in content


class TestView:
    def test_format_size_bytes(self):
        view = View()
        assert view._format_size(500) == "500.0 B"

    def test_format_size_kilobytes(self):
        view = View()
        assert view._format_size(2048) == "2.0 KB"

    def test_format_size_megabytes(self):
        view = View()
        assert view._format_size(2097152) == "2.0 MB"


class TestController:
    @pytest.fixture
    def temp_dir(self):
        temp = tempfile.mkdtemp()
        yield Path(temp)
        shutil.rmtree(temp)

    @pytest.fixture
    def controller_with_files(self, temp_dir):
        (temp_dir / "file1.txt").write_text("content1")
        (temp_dir / "file2.txt").write_text("content2")

        view = View()
        controller = Controller(view)
        controller.set_directory(str(temp_dir))
        controller.scan_directory()

        return controller

    def test_set_directory(self, temp_dir, monkeypatch):
        inputs = iter(["test"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        view = View()
        controller = Controller(view)
        result = controller.set_directory(str(temp_dir))

        assert result is True
        assert controller.model is not None

    def test_scan_directory(self, temp_dir):
        (temp_dir / "test.txt").write_text("content")

        view = View()
        controller = Controller(view)
        controller.set_directory(str(temp_dir))
        result = controller.scan_directory()

        assert result is True
        assert len(controller.current_files) == 1

    def test_show_files(self, temp_dir, capsys):
        (temp_dir / "test.txt").write_text("content")

        view = View()
        controller = Controller(view)
        controller.set_directory(str(temp_dir))
        controller.scan_directory()
        controller.show_files()

        captured = capsys.readouterr()
        assert "test.txt" in captured.out
        assert "1" in captured.out

    def test_classify_files(self, temp_dir, capsys):
        (temp_dir / "doc.txt").write_text("1")
        (temp_dir / "doc.pdf").write_text("2")

        view = View()
        controller = Controller(view)
        controller.set_directory(str(temp_dir))
        controller.scan_directory()
        controller.classify_files()

        captured = capsys.readouterr()
        assert ".txt" in captured.out
        assert ".pdf" in captured.out

    def test_delete_by_name(self, temp_dir):
        (temp_dir / "file1.txt").write_text("content1")
        (temp_dir / "file2.txt").write_text("content2")

        view = View()
        controller = Controller(view)
        controller.set_directory(str(temp_dir))
        controller.scan_directory()

        found, not_found = controller.model.get_files_by_names(["file1.txt"])

        assert len(found) == 1
        assert found[0].name == "file1.txt"
