from pos_extractor import cli


def test_cli_missing_file(capsys):
    exit_code = cli.main(["missing.txt"])
    captured = capsys.readouterr()
    assert exit_code == 2
    assert "file not found" in captured.err.lower()


def test_cli_model_error(capsys, monkeypatch, tmp_path):
    sample = tmp_path / "sample.txt"
    sample.write_text("text", encoding="utf-8")

    def _raise_runtime_error(_path):
        raise RuntimeError("spaCy model missing")

    monkeypatch.setattr(cli, "extract_from_file", _raise_runtime_error)
    exit_code = cli.main([str(sample)])
    captured = capsys.readouterr()
    assert exit_code == 2
    assert "spacy model missing" in captured.err.lower()
