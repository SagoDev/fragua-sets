"""StepBuilders for load functions."""

from typing import Dict
from fragua_sets.core.step_builder import StepBuilder
from fragua_sets.utils.enums.functions import LoadFunction
from fragua_sets.utils.enums.sets import Sets

SET_NAME = Sets.LOADING.value
LoadFunc = LoadFunction

LOAD_TO_CSV = StepBuilder(
    set_name=SET_NAME,
    function=LoadFunc.LOAD_TO_CSV.value,
)

LOAD_TO_EXCEL = StepBuilder(
    set_name=SET_NAME,
    function=LoadFunc.LOAD_TO_EXCEL.value,
)

LOAD_TO_API = StepBuilder(
    set_name=SET_NAME,
    function=LoadFunc.LOAD_TO_API.value,
)

LOAD_TO_BD = StepBuilder(
    set_name=SET_NAME,
    function=LoadFunc.LOAD_TO_DB.value,
)

LOADING_STEPS: Dict[str, StepBuilder] = {
    LoadFunc.LOAD_TO_API.value: LOAD_TO_API,
    LoadFunc.LOAD_TO_DB.value: LOAD_TO_BD,
    LoadFunc.LOAD_TO_CSV.value: LOAD_TO_CSV,
    LoadFunc.LOAD_TO_EXCEL.value: LOAD_TO_EXCEL,
}
