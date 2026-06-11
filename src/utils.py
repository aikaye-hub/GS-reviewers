"""Utility functions for loading and processing data."""

import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)


class DataLoader:
    """Handles loading and caching of data files."""
    
    def __init__(self, data_dir: str = "data"):
        """Initialize DataLoader.
        
        Args:
            data_dir: Directory containing JSON data files
        """
        self.data_dir = Path(data_dir)
        self._cards_cache: Optional[List[Dict]] = None
        self._references_cache: Optional[List[Dict]] = None
    
    def load_cards(self, force_reload: bool = False) -> List[Dict[str, Any]]:
        """Load cards from JSON file.
        
        Args:
            force_reload: Force reload from disk, ignore cache
            
        Returns:
            List of card dictionaries
            
        Raises:
            FileNotFoundError: If cards.json not found
            json.JSONDecodeError: If JSON is invalid
        """
        if self._cards_cache and not force_reload:
            return self._cards_cache
        
        filepath = self.data_dir / "cards.json"
        
        if not filepath.exists():
            raise FileNotFoundError(f"Cards file not found: {filepath}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self._cards_cache = json.load(f)
            logger.info(f"Loaded {len(self._cards_cache)} cards from {filepath}")
            return self._cards_cache
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {filepath}: {e}")
            raise
    
    def load_references(self, force_reload: bool = False) -> List[Dict[str, Any]]:
        """Load references from JSON file.
        
        Args:
            force_reload: Force reload from disk, ignore cache
            
        Returns:
            List of reference topic dictionaries
            
        Raises:
            FileNotFoundError: If references.json not found
            json.JSONDecodeError: If JSON is invalid
        """
        if self._references_cache and not force_reload:
            return self._references_cache
        
        filepath = self.data_dir / "references.json"
        
        if not filepath.exists():
            raise FileNotFoundError(f"References file not found: {filepath}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self._references_cache = json.load(f)
            logger.info(f"Loaded {len(self._references_cache)} references from {filepath}")
            return self._references_cache
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {filepath}: {e}")
            raise
    
    def get_cards_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Get all cards for a specific category.
        
        Args:
            category: Category name (e.g., "Appendicitis")
            
        Returns:
            List of cards in that category
        """
        cards = self.load_cards()
        return [c for c in cards if c.get('cat') == category]
    
    def get_reference_by_topic(self, topic: str) -> Optional[Dict[str, Any]]:
        """Get reference by topic name.
        
        Args:
            topic: Topic name (e.g., "Hernia")
            
        Returns:
            Reference dictionary or None if not found
        """
        references = self.load_references()
        for ref in references:
            if ref.get('topic') == topic:
                return ref
        return None
    
    def get_all_categories(self) -> List[str]:
        """Get list of all unique card categories.
        
        Returns:
            Sorted list of category names
        """
        cards = self.load_cards()
        categories = set(c.get('cat') for c in cards if 'cat' in c)
        return sorted(categories)


def setup_logging(level: int = logging.INFO) -> None:
    """Setup basic logging configuration.
    
    Args:
        level: Logging level (default: INFO)
    """
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
