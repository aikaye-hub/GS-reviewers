"""Validation functions for surgical education data."""

import logging
from typing import List, Dict, Any, Tuple

logger = logging.getLogger(__name__)


def validate_card(card: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate a single card against required fields.
    
    Args:
        card: Card dictionary to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    required_fields = {'id', 'cat', 'q', 'source', 'correct', 'choices'}
    missing = required_fields - set(card.keys())
    
    if missing:
        return False, f"Missing fields: {missing}"
    
    # Validate types
    if not isinstance(card['id'], int):
        return False, "id must be integer"
    
    if not isinstance(card['choices'], list) or len(card['choices']) < 2:
        return False, "choices must be list with at least 2 items"
    
    if not isinstance(card['q'], str) or not card['q'].strip():
        return False, "question must be non-empty string"
    
    # Validate correct answer is in choices
    if card['correct'] not in card['choices']:
        return False, f"correct answer not in choices: {card['correct']}"
    
    return True, ""


def validate_cards(cards: List[Dict[str, Any]]) -> Tuple[List[Dict], List[str]]:
    """Validate entire cards collection.
    
    Args:
        cards: List of card dictionaries
        
    Returns:
        Tuple of (valid_cards, error_messages)
    """
    valid_cards = []
    errors = []
    
    for idx, card in enumerate(cards):
        is_valid, error_msg = validate_card(card)
        
        if is_valid:
            valid_cards.append(card)
        else:
            error = f"Card {idx} (id={card.get('id', 'unknown')}): {error_msg}"
            errors.append(error)
            logger.warning(error)
    
    return valid_cards, errors


def validate_reference_table(section: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate a reference table structure.
    
    Args:
        section: Reference section with table
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if 'table' not in section:
        return False, "Missing 'table' key"
    
    table = section['table']
    
    if 'headers' not in table or 'rows' not in table:
        return False, "Table missing 'headers' or 'rows'"
    
    headers = table['headers']
    rows = table['rows']
    
    if not isinstance(headers, list) or len(headers) == 0:
        return False, "Headers must be non-empty list"
    
    if not isinstance(rows, list):
        return False, "Rows must be list"
    
    # Validate row column count matches headers
    for row_idx, row in enumerate(rows):
        if not isinstance(row, list):
            return False, f"Row {row_idx} is not a list"
        
        if len(row) != len(headers):
            return False, (
                f"Row {row_idx} has {len(row)} columns, "
                f"expected {len(headers)}"
            )
    
    return True, ""


def validate_reference_topic(topic: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate a reference topic structure.
    
    Args:
        topic: Reference topic dictionary
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    required = {'topic', 'color', 'sections'}
    missing = required - set(topic.keys())
    
    if missing:
        return False, f"Missing fields: {missing}"
    
    if not isinstance(topic['sections'], list):
        return False, "sections must be list"
    
    for sec_idx, section in enumerate(topic['sections']):
        is_valid, error = validate_reference_table(section)
        if not is_valid:
            return False, f"Section {sec_idx} ({section.get('title', 'unknown')}): {error}"
    
    return True, ""


def validate_references(references: List[Dict[str, Any]]) -> Tuple[List[Dict], List[str]]:
    """Validate entire references collection.
    
    Args:
        references: List of reference topic dictionaries
        
    Returns:
        Tuple of (valid_references, error_messages)
    """
    valid_refs = []
    errors = []
    
    for idx, ref in enumerate(references):
        is_valid, error_msg = validate_reference_topic(ref)
        
        if is_valid:
            valid_refs.append(ref)
        else:
            error = f"Reference {idx} ({ref.get('topic', 'unknown')}): {error_msg}"
            errors.append(error)
            logger.warning(error)
    
    return valid_refs, errors
