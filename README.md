# POS Extractor

Simple Python CLI that extracts unique nouns and verbs from a text file using spaCy POS tagging.

## Requirements

- Python 3.11+

## Installation

```bash
python -m pip install --upgrade pip
pip install .
python -m spacy download en_core_web_sm
```

For development/tests:

```bash
pip install .[dev]
```

## Usage

Using console script:

```bash
pos-extract path/to/input.txt
```

Using module execution:

```bash
python -m pos_extractor path/to/input.txt
```

Help:

```bash
pos-extract --help
```

Output includes separate noun/verb lists with unique tokens in deterministic sorted order and counts.
