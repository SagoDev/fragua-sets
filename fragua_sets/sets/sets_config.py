"""Configuration for Sets."""

from typing import Any, Callable, Dict, Iterable, List, Optional, Union

from fragua import FraguaRegistry, FraguaSet, FraguaPipeline

from fragua_sets.functions.extraction import EXTRACTION_FUNCTIONS
from fragua_sets.functions.loading import LOADING_FUNCTIONS
from fragua_sets.functions.utility import UTILITY_FUNCTIONS

FUNCTION_LISTS: Dict[str, Any] = {
    "extraction": EXTRACTION_FUNCTIONS,
    "loading": LOADING_FUNCTIONS,
    "utility": UTILITY_FUNCTIONS,
}


def create_set(
    name: str,
    items: Iterable[Union[Callable[..., Any], FraguaPipeline]],
) -> FraguaSet:
    """
    Create a FraguaSet from a collection of callables and/or pipelines.

    Functions are registered using their __name__.
    Pipelines are registered using their pipeline name.

    Parameters
    ----------
    name:
        Name of the FraguaSet.
    items:
        Iterable of callables or FraguaPipeline instances.

    Returns
    -------
    FraguaSet
        A FraguaSet containing the registered items.

    Raises
    ------
    ValueError
        If an item has no valid name, is not supported,
        or a name collision occurs.
    """
    fragua_set = FraguaSet(name=name)

    for item in items:
        # Case 1: Pipeline
        if isinstance(item, FraguaPipeline):
            item_name = item.name

            if not item_name:
                raise ValueError(f"Pipeline has no valid name: {item!r}")

            registered = fragua_set.register(item_name, item)
            if not registered:
                raise ValueError(
                    f"Duplicate pipeline name '{item_name}' in FraguaSet '{name}'"
                )

            continue

        # Case 2: Callable
        if callable(item):
            item_name: Optional[str] = getattr(item, "__name__", None)
            # Reject anonymous or invalid callables (e.g. lambdas)
            if not item_name:
                raise ValueError(f"Callable has no valid __name__: {item!r}")

            registered = fragua_set.register(item_name, item)
            if not registered:
                raise ValueError(
                    f"Duplicate function name '{item_name}' in FraguaSet '{name}'"
                )

            continue

        # Unsupported type
        raise ValueError(
            f"Unsupported item type '{type(item).__name__}' in FraguaSet '{name}'"
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

    for set_name, items in FUNCTION_LISTS.items():
        # Create a FraguaSet using the single-set factory
        fragua_set = create_set(
            name=set_name,
            items=items,
        )
        sets.append(fragua_set)

    return sets


def add_sets_to_registry(
    sets: Iterable[FraguaSet],
    registry: FraguaRegistry,
    replace_sets: bool = False,
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

        if replace_sets and not registered:
            registry.replace_set(fragua_set)
            return

        # Fail explicitly on name collision
        if not registered:
            raise ValueError(
                f"FraguaSet '{fragua_set.name}' is already registered "
                f"in the FraguaRegistry"
            )


SETS_LIST = create_sets_list()
