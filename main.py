"""Main File."""

import fragua as fg
from fragua_sets.sets.sets_config import FRAGUA_SETS

# Create fragua environment
env = fg.FraguaEnvironment("env-example")

# Add pre-configurated fragua sets
for fg_set in FRAGUA_SETS:
    env.registry.add_set(fg_set)


# Print some lists to the console to see if the sets and functions are being saved correctly.
all_sets = env.registry.list_sets()

for set_name in all_sets:
    fg_set = env.registry.get_set(set_name)
    if fg_set is None:
        continue
    print(f"Set: {fg_set.name}")
    print("Functions:", fg_set.list())
    print("-" * 40)
