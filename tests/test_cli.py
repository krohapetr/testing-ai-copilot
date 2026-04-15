from pos_extractor import cli


def test_cli_missing_file(capsys):
    exit_code = cli.main(["missing.txt"])
    captured = capsys.readouterr()
    assert exit_code == 2
    assert "file not found" in captured.err.lower()
