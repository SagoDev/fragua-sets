"""Enums classes type."""

from enum import Enum


# ----------------------------
# EXTRACTION FUNCTIONS
# ----------------------------
class ExtractionFunction(str, Enum):
    """Extraction function types."""

    EXTRACT_FROM_CSV = "extract_from_csv"
    EXTRACT_FROM_EXCEL = "extract_from_excel"
    EXTRACT_FROM_API = "extract_from_api"
    EXTRACT_FROM_DB = "extract_from_database"


# ----------------------------
# LOAD FUNCTIONS
# ----------------------------
class LoadFunction(str, Enum):
    """Extraction function types."""

    LOAD_TO_CSV = "load_to_csv"
    LOAD_TO_EXCEL = "load_to_excel"
    LOAD_TO_API = "load_to_api"
    LOAD_TO_DB = "load_to_database"
