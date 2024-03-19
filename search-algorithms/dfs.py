"""
Copyright (c) 2024 Adventune. All Rights Reserved.

Depth-first search algorithm for the Goat and Cabbage problem.

The problem is as follows:
A farmer wants to cross a river and take with him a wolf, a goat, and a cabbage.
There is a boat that can fit the farmer plus either the wolf, the goat, or the cabbage.
If the wolf and the goat are alone on one side of the river, the wolf will eat the goat.
If the goat and the cabbage are alone on the same side, the goat will eat the cabbage.
How can the farmer bring the wolf, the goat, and the cabbage across the river?

Depth-first search is used to find a solution to the problem.
"""

import json
from queue import Queue

from helpers import hash_state, valid_state, wordify_path

# State is represented as {"farmer": False, "goat": False, "cabbage": False, "wolf": False}
# G - Goat
# C - Cabbage
# W - Wolf
# F - Farmer
# False - Left side


def get_neighbors(state):
    """
    Get all valid neighbors of the state
    """
    new_states = []
    # Farmer can move alone, with the goat, with the cabbage, or with the wolf
    for key in state:
        new_state = state.copy()
        if key == "F":
            new_state["F"] = not new_state["F"]
            if valid_state(new_state):
                new_states.append(new_state)
        else:
            if new_state["F"] == new_state[key]:
                new_state[key] = not new_state[key]
                new_state["F"] = not new_state["F"]
                if valid_state(new_state):
                    new_states.append(new_state)

    return new_states


if __name__ == "__main__":
    # Initial state, all on the left side
    starting_state = {"F": False, "G": False, "C": False, "W": False}

    # Stack to store the states
    stack = []
    stack.append((starting_state, [starting_state]))
    visited = set()
    visited.add(hash_state(starting_state))

    while stack:

        state = stack.pop(-1)
        if all(state[0].values()):
            print("Solution found!")
            print("\n".join(wordify_path(state[1])))
            break
        neighbors = get_neighbors(state[0])
        for neighbor in neighbors:
            if hash_state(neighbor) not in visited:
                stack.append((neighbor, state[1] + [neighbor]))
                visited.add(hash_state(neighbor))
