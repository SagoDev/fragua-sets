"""StepBuilders for extraction functions."""

from typing import Dict
from fragua_sets.core.step_builder import StepBuilder
from fragua_sets.utils.enums.functions import ExtractionFunction
from fragua_sets.utils.enums.sets import Sets

SET_NAME = Sets.EXTRACTION.value
ExtFunc = ExtractionFunction

EXTRACT_FROM_CSV = StepBuilder(
    set_name=SET_NAME,
    function=ExtFunc.EXTRACT_FROM_CSV.value,
)

EXTRACT_FROM_EXCEL = StepBuilder(
    set_name=SET_NAME,
    function=ExtFunc.EXTRACT_FROM_EXCEL.value,
)

EXTRACT_FROM_API = StepBuilder(
    set_name=SET_NAME,
    function=ExtFunc.EXTRACT_FROM_API.value,
)

EXTRACT_FROM_BD = StepBuilder(
    set_name=SET_NAME,
    function=ExtFunc.EXTRACT_FROM_DB.value,
)

EXTRACTION_STEPS: Dict[str, StepBuilder] = {
    ExtFunc.EXTRACT_FROM_API.value: EXTRACT_FROM_API,
    ExtFunc.EXTRACT_FROM_DB.value: EXTRACT_FROM_BD,
    ExtFunc.EXTRACT_FROM_CSV.value: EXTRACT_FROM_CSV,
    ExtFunc.EXTRACT_FROM_EXCEL.value: EXTRACT_FROM_EXCEL,
}
