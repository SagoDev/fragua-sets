"""Pipelines config."""

from typing import List

from fragua import FraguaPipeline

from .excel_to_csv import excel_to_csv


PIPELINES_FUNCTIONS: List[FraguaPipeline] = [
    excel_to_csv,
]
