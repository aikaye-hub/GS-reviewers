"""Data models for surgical education cards and references."""

from typing import List, Dict, Any, TypedDict


class CardChoice(TypedDict, total=False):
    """A single multiple choice option."""
    text: str


class Card(TypedDict, total=False):
    """A surgical education quiz card."""
    id: int
    cat: str  # category
    q: str  # question
    source: str
    correct: str
    choices: List[str]


class TableRow(TypedDict):
    """A row in a reference table."""
    pass  # List[str]


class ReferenceTable(TypedDict):
    """A table within a reference section."""
    headers: List[str]
    rows: List[List[str]]


class ReferenceSection(TypedDict, total=False):
    """A section within a reference topic."""
    title: str
    table: ReferenceTable


class ReferenceTopic(TypedDict, total=False):
    """A complete reference topic with tables."""
    topic: str
    color: str
    sections: List[ReferenceSection]


class DataStore(TypedDict, total=False):
    """Complete data store."""
    cards: List[Card]
    references: List[ReferenceTopic]
