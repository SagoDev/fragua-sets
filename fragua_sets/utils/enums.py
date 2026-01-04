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
# LOAD INTERNAL FUNCTIONS
# ----------------------------


class ILF(str, Enum):
    """Internal Load Functions."""

    VALIDATE_LOAD = "validate_load"
    VALIDATE_SQL_LOAD = "validate_sql_load"
    VALIDATE_API_LOAD = "validate_api_load"
    BUILD_PATH = "build_path"
    CONVERT_DATETIME_COLUMNS = "convert_datetime_columns"
    WRITE_EXCEL = "write_excel"
    WRITE_CSV = "write_csv"
    WRITE_SQL = "write_sql"
    WRITE_API = "write_api"
