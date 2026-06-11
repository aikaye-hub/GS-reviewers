"""Main application module - refactored from generate_app.py"""

import logging
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from src.utils import DataLoader, setup_logging
from src.validators import validate_cards, validate_references

logger = logging.getLogger(__name__)


def main():
    """Main entry point for the application."""
    setup_logging()
    
    try:
        # Initialize data loader
        loader = DataLoader(data_dir="data")
        
        logger.info("=" * 60)
        logger.info("Surgical Education App - Data Loading")
        logger.info("=" * 60)
        
        # Load cards
        logger.info("\nLoading cards...")
        cards = loader.load_cards()
        valid_cards, card_errors = validate_cards(cards)
        
        if card_errors:
            logger.warning(f"Found {len(card_errors)} invalid cards:")
            for error in card_errors:
                logger.warning(f"  - {error}")
        
        logger.info(f"✓ Loaded {len(valid_cards)} valid cards")
        
        # Load references
        logger.info("\nLoading references...")
        references = loader.load_references()
        valid_refs, ref_errors = validate_references(references)
        
        if ref_errors:
            logger.warning(f"Found {len(ref_errors)} invalid references:")
            for error in ref_errors:
                logger.warning(f"  - {error}")
        
        logger.info(f"✓ Loaded {len(valid_refs)} valid reference topics")
        
        # Print statistics
        logger.info("\n" + "=" * 60)
        logger.info("Data Statistics")
        logger.info("=" * 60)
        
        categories = loader.get_all_categories()
        logger.info(f"\nCard Categories ({len(categories)}):")
        for cat in categories:
            count = len(loader.get_cards_by_category(cat))
            logger.info(f"  • {cat}: {count} cards")
        
        logger.info(f"\nReference Topics ({len(valid_refs)}):")
        for ref in valid_refs:
            section_count = len(ref.get('sections', []))
            logger.info(f"  • {ref['topic']}: {section_count} sections")
        
        logger.info("\n" + "=" * 60)
        logger.info("✓ Data loading complete!")
        logger.info("=" * 60 + "\n")
        
        return 0
    
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
