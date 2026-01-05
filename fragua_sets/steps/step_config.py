"""Configuration for creation of FraguaStep."""

from fragua_sets.core.step_index import StepIndex
from fragua_sets.steps.extraction import EXTRACTION_STEPS
from fragua_sets.steps.loading import LOADING_STEPS
from fragua_sets.steps.utility import UTILITY_STEPS

DICTS_LIST = [EXTRACTION_STEPS, LOADING_STEPS, UTILITY_STEPS]


def create_step_index() -> StepIndex:
    """Create fragua-sets step index."""
    step_index = StepIndex()

    for step_dict in DICTS_LIST:
        for name, step in step_dict.items():
            step_index.register(name=name, builder=step)

    return step_index


STEP_INDEX = create_step_index()
