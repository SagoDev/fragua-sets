"""Configuration for Sets."""

from typing import Any, Dict, List
from fragua import FraguaSet

from fragua_sets.functions.extraction import EXTRACTION_FUNCTIONS
from fragua_sets.functions.loading import LOADING_FUNCTIONS
from fragua_sets.functions.transformation import TRANSFORMATION_FUNCTIONS
from fragua_sets.functions.utility import UTILITY_FUNCTIONS

FUNCTION_LISTS: Dict[str, Dict[str, Any]] = {
    "extraction": {"functions": EXTRACTION_FUNCTIONS},
    "transformation": {"functions": TRANSFORMATION_FUNCTIONS},
    "loading": {"functions": LOADING_FUNCTIONS},
    "utility": {"functions": UTILITY_FUNCTIONS, "step_enabled": False},
}


def create_sets() -> List[FraguaSet]:
    """Create fragua set list."""
    func_lists = FUNCTION_LISTS
    sets_list: List[FraguaSet] = []

    for set_name, items in func_lists.items():
        func_set = FraguaSet(
            name=set_name,
            items=items["functions"],
            step_enabled=items["step_enabled"] if items["step_enabled"] else True,
        )
        sets_list.append(func_set)

    return sets_list


SETS_LIST: List[FraguaSet] = create_sets()
