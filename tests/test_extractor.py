from pos_extractor.extractor import extract_from_file, extract_nouns_and_verbs


class FakeToken:
    def __init__(self, lemma: str, pos: str, is_alpha: bool = True):
        self.lemma_ = lemma
        self.pos_ = pos
        self.is_alpha = is_alpha


def test_extract_nouns_and_verbs_unique_sorted():
    def fake_nlp(_: str):
        return [
            FakeToken("dogs", "NOUN"),
            FakeToken("dog", "NOUN"),
            FakeToken("run", "VERB"),
            FakeToken("Run", "VERB"),
            FakeToken("Alice", "PROPN"),
            FakeToken("123", "NOUN", is_alpha=False),
            FakeToken("!", "PUNCT", is_alpha=False),
        ]

    nouns, verbs = extract_nouns_and_verbs("ignored", nlp=fake_nlp)
    assert nouns == ["alice", "dog", "dogs"]
    assert verbs == ["run"]


def test_extract_from_file_reads_text(tmp_path):
    sample = tmp_path / "input.txt"
    sample.write_text("Dogs run.", encoding="utf-8")

    def fake_nlp(_text: str):
        return [FakeToken("dog", "NOUN"), FakeToken("run", "VERB")]

    nouns, verbs = extract_from_file(sample, nlp=fake_nlp)
    assert nouns == ["dog"]
    assert verbs == ["run"]
