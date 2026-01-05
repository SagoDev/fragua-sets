"""Steps of utility functions."""

from typing import Dict
from fragua_sets.core.step_builder import StepBuilder
from fragua_sets.utils.enums.functions import UtilityFunction
from fragua_sets.utils.enums.sets import Sets

SET_NAME = Sets.UTILITY.value
UtFunc = UtilityFunction

PATH_EXISTS = StepBuilder(set_name=SET_NAME, function=UtFunc.PATH_EXISTS.value)

ENSURE_DIR_EXISTS = StepBuilder(
    set_name=SET_NAME, function=UtFunc.ENSURE_DIR_EXISTS.value
)

ENSURE_PARENT_DIR_EXISTS = StepBuilder(
    set_name=SET_NAME, function=UtFunc.ENSURE_PARENT_DIR_EXISTS.value
)

UTILITY_STEPS: Dict[str, StepBuilder] = {
    UtFunc.PATH_EXISTS.value: PATH_EXISTS,
    UtFunc.ENSURE_DIR_EXISTS.value: ENSURE_DIR_EXISTS,
    UtFunc.ENSURE_PARENT_DIR_EXISTS.value: ENSURE_PARENT_DIR_EXISTS,
}
