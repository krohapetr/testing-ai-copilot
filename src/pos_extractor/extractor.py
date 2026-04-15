from pathlib import Path


def load_nlp(model: str = "en_core_web_sm"):
    try:
        import spacy
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError(
            "spaCy is not installed. Install dependencies with `pip install .`."
        ) from exc

    try:
        return spacy.load(model)
    except OSError as exc:
        raise RuntimeError(
            "spaCy model 'en_core_web_sm' is not installed. "
            "Install it with: python -m spacy download en_core_web_sm"
        ) from exc


def extract_nouns_and_verbs(text: str, *, nlp=None) -> tuple[list[str], list[str]]:
    nlp = nlp or load_nlp()
    doc = nlp(text)

    nouns = sorted(
        {token.lemma_.lower() for token in doc if token.pos_ in {"NOUN", "PROPN"} and token.is_alpha}
    )
    verbs = sorted(
        {token.lemma_.lower() for token in doc if token.pos_ == "VERB" and token.is_alpha}
    )
    return nouns, verbs


def extract_from_file(path: str | Path, *, nlp=None) -> tuple[list[str], list[str]]:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    return extract_nouns_and_verbs(text, nlp=nlp)
