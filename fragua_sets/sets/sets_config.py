"""Configuration for Sets."""

from typing import Any, Callable, Dict, Iterable, List

from fragua import FraguaRegistry, FraguaSet

from fragua_sets.functions.extraction import EXTRACTION_FUNCTIONS
from fragua_sets.functions.loading import LOADING_FUNCTIONS
from fragua_sets.functions.utility import UTILITY_FUNCTIONS

FUNCTION_LISTS: Dict[str, Iterable[Callable[..., Any]]] = {
    "extraction": EXTRACTION_FUNCTIONS,
    "loading": LOADING_FUNCTIONS,
    "utility": UTILITY_FUNCTIONS,
}


def create_functions_set(
    name: str,
    functions: Iterable[Callable[..., Any]],
) -> FraguaSet:
    """
    Create a FraguaSet from a collection of callables.

    Each callable is registered in the set using its function name.
    The function name must be unique within the set.

    Parameters
    ----------
    name:
        Name of the FraguaSet.
    functions:
        Iterable of callable objects to register.

    Returns
    -------
    FraguaSet
        A FraguaSet containing the provided functions.

    Raises
    ------
    ValueError
        If a callable does not have a valid name or if a name collision occurs.
    """
    fragua_set = FraguaSet(name=name)

    for func in functions:
        # Ensure the object is callable
        if not callable(func):
            raise ValueError(f"Object is not callable: {func!r}")

        func_name = getattr(func, "__name__", None)

        # Reject callables without a proper name (e.g. lambdas)
        if not func_name:
            raise ValueError(f"Callable has no valid __name__: {func!r}")

        # Register function, fail explicitly on collision
        registered = fragua_set.register(func_name, func)
        if not registered:
            raise ValueError(
                f"Duplicate function name '{func_name}' in FraguaSet '{name}'"
            )

    return fragua_set


def create_sets_list() -> List[FraguaSet]:
    """
    Create multiple FraguaSets from a dictionary definition.

    Each dictionary key represents the name of a FraguaSet, and
    each value is an iterable of callables to be registered in
    the corresponding set.

    Parameters
    ----------
    definitions:
        Mapping of set names to iterables of callables.

    Returns
    -------
    list[FraguaSet]
        List of created FraguaSet instances.

    Raises
    ------
    ValueError
        If any definition is invalid or if a function registration fails.
    """
    sets: List[FraguaSet] = []

    for set_name, functions in FUNCTION_LISTS.items():
        # Create a FraguaSet using the single-set factory
        fragua_set = create_functions_set(
            name=set_name,
            functions=functions,
        )
        sets.append(fragua_set)

    return sets


def add_sets_to_registry(
    sets: Iterable[FraguaSet],
    registry: FraguaRegistry,
) -> None:
    """
    Register multiple FraguaSet instances into a FraguaRegistry.

    Each FraguaSet is registered in the registry using its name.
    Registration fails explicitly if a set name already exists
    in the registry.

    Parameters
    ----------
    sets:
        Iterable of FraguaSet instances to register.
    registry:
        Target FraguaRegistry.

    Raises
    ------
    ValueError
        If a set cannot be registered due to a name collision.
    """
    for fragua_set in sets:
        # Attempt to register the set using its name
        registered = registry.add_set(fragua_set)

        # Fail explicitly on name collision
        if not registered:
            raise ValueError(
                f"FraguaSet '{fragua_set.name}' is already registered "
                f"in the FraguaRegistry"
            )


SETS_LIST = create_sets_list()
