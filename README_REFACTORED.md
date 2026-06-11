# Surgical Education Reviewer - Refactored

## Overview

This project has been refactored to separate concerns and improve maintainability. Data is now externalized from code, with proper validation and type hints throughout.

## Project Structure

```
├── generate_app.py          # Main entry point (refactored)
├── data/
│   ├── cards.json          # Quiz card data
│   └── references.json     # Reference table data
├── src/
│   ├── __init__.py
│   ├── models.py           # Type definitions
│   ├── validators.py       # Data validation functions
│   └── utils.py            # Data loading utilities
└── README.md               # This file
```

## Key Improvements

### 1. **Separation of Concerns**
- **Data** (JSON files) is separate from **Logic** (Python modules)
- Easy to update data without touching code
- Supports hot-reloading and external data management

### 2. **Type Safety**
- All functions have type hints (`src/models.py`)
- Better IDE support and static analysis
- Clear function contracts

### 3. **Data Validation**
- Comprehensive validation in `src/validators.py`
- Validates card completeness, choices consistency, and reference table structure
- Detailed error reporting for debugging

### 4. **Caching and Performance**
- `DataLoader` class caches loaded data
- Optional force-reload capability
- Category and topic lookups optimized

### 5. **Error Handling**
- Proper exception handling with logging
- Graceful degradation on missing files
- Clear error messages for debugging

### 6. **Logging**
- Structured logging using Python's `logging` module
- Info, warning, and error levels
- Timestamps and module names for traceability

## Usage

### Basic Usage

```bash
python generate_app.py
```

### Output Example

```
============================================================
Surgical Education App - Data Loading
============================================================

Loading cards...
✓ Loaded 210 valid cards

Loading references...
✓ Loaded 15 valid reference topics

============================================================
Data Statistics
============================================================

Card Categories (15):
  • Appendicitis: 18 cards
  • Hernia: 15 cards
  • Trauma: 15 cards
  ...
```

### Using DataLoader in Your Code

```python
from src.utils import DataLoader

# Initialize
loader = DataLoader(data_dir="data")

# Load all cards
cards = loader.load_cards()

# Get cards by category
appendicitis_cards = loader.get_cards_by_category("Appendicitis")

# Get reference by topic
hernia_ref = loader.get_reference_by_topic("Hernia")

# Get all categories
categories = loader.get_all_categories()
```

### Validating Data

```python
from src.validators import validate_cards, validate_references

valid_cards, errors = validate_cards(my_cards)
if errors:
    for error in errors:
        print(f"Validation error: {error}")
```

## Data Format

### Cards (data/cards.json)

```json
[
  {
    "id": 16,
    "cat": "Appendicitis",
    "q": "An Alvarado score of 8 would suggest:",
    "source": "Alvarado 1986",
    "correct": "High probability of appendicitis",
    "choices": [
      "High probability of appendicitis",
      "Low probability; conservative management",
      "Borderline; further imaging needed"
    ]
  }
]
```

### References (data/references.json)

```json
[
  {
    "topic": "Hernia",
    "color": "#1A3C6E",
    "sections": [
      {
        "title": "Hiatal Hernia Types",
        "table": {
          "headers": ["Type", "Description", "Surgery?"],
          "rows": [
            ["I — Sliding", "GEJ slides above diaphragm (95%)", "Symptomatic only"],
            ["II — Paraesophageal", "GEJ normal, fundus herniates", "Yes — volvulus risk"]
          ]
        }
      }
    ]
  }
]
```

## Testing

Run validation on your data:

```python
python -c "
from src.utils import DataLoader, setup_logging
from src.validators import validate_cards, validate_references

setup_logging()
loader = DataLoader()

cards = loader.load_cards()
refs = loader.load_references()

valid_c, c_errors = validate_cards(cards)
valid_r, r_errors = validate_references(refs)

print(f'Valid cards: {len(valid_c)}, Errors: {len(c_errors)}')
print(f'Valid refs: {len(valid_r)}, Errors: {len(r_errors)}')
"
```

## Migration from Old Code

The old `generate_app.py` had:
- **2,700+ lines** with hardcoded data
- Data and logic mixed together
- No validation
- No type hints
- No error handling

The refactored version:
- **Clean separation** of concerns
- **Modular design** with reusable components
- **Comprehensive validation**
- **Full type hints** for better tooling
- **Proper error handling** and logging
- **Extensible architecture** for future features

## Future Enhancements

1. **Database Support** - Replace JSON with SQLite/PostgreSQL
2. **API Endpoint** - Flask/FastAPI wrapper for web access
3. **Admin Interface** - Web UI for managing cards and references
4. **Search Functionality** - Full-text search across all cards
5. **Performance Metrics** - Track user scores and card difficulty
6. **Export Features** - Export to PDF, Excel, etc.

## Contributing

When adding new data:

1. Update `data/cards.json` or `data/references.json`
2. Run validation: `python generate_app.py`
3. Check for errors in the output
4. Commit with clear message

## License

[Your License Here]
