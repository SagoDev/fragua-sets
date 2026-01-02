"""Enums classes type."""

from enum import Enum


# ----------------------------
# TRANSFORM INTERNAL FUNCTIONS
# ----------------------------


class ITF(str, Enum):
    """Internal Transform Functions."""

    FILL_MISSING = "fill_missing"
    STANDARDIZE = "standardize"
    ENCODE_CATEGORICALS = "encode_categoricals"
    SCALE_NUMERIC = "scale_numeric"
    TREAT_OUTLIERS = "treat_outliers"
    ADD_DERIVED_COLUMNS = "add_derived_columns"
    FORMAT_NUMERIC = "format_numeric"
    GROUP_AND_AGGREGATE = "group_and_aggregate"
    SORT_DATAFRAME = "sort_dataframe"


class ITFConfigKeys(str, Enum):
    """Internal transform function config keys."""

    NUMERIC_FILL = "numeric_fill"
    CATEGORICAL_FILL = "categorical_fill"
    OUTLIER_THRESHOLD = "outlier_threshold"
    DERIVED_COLUMNS = "derived_columns"
    ROUNDING_PRECISION = "rounding_precision"
    GROUP_BY_COLS = "group_by_cols"
    AGG_FUNCTIONS = "agg_functions"
    SORT_BY = "sort_by"


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
