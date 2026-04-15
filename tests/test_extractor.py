from pos_extractor.extractor import extract_nouns_and_verbs


class _Token:
    def __init__(self, lemma: str, pos: str, is_alpha: bool = True):
        self.lemma_ = lemma
        self.pos_ = pos
        self.is_alpha = is_alpha


def test_extract_nouns_and_verbs_unique_sorted():
    def fake_nlp(_text: str):
        return [
            _Token("dogs", "NOUN"),
            _Token("dog", "NOUN"),
            _Token("run", "VERB"),
            _Token("Run", "VERB"),
            _Token("Alice", "PROPN"),
            _Token("123", "NOUN", is_alpha=False),
            _Token("!", "PUNCT", is_alpha=False),
        ]

    nouns, verbs = extract_nouns_and_verbs("ignored", nlp=fake_nlp)
    assert nouns == ["alice", "dog", "dogs"]
    assert verbs == ["run"]
