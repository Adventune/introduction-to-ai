"""
Copyright (c) 2024 Adventune. All Rights Reserved.

Breadth-first search algorithm for the Goat and Cabbage problem.

The problem is as follows:
A farmer wants to cross a river and take with him a wolf, a goat, and a cabbage.
There is a boat that can fit the farmer plus either the wolf, the goat, or the cabbage.
If the wolf and the goat are alone on one side of the river, the wolf will eat the goat.
If the goat and the cabbage are alone on the same side, the goat will eat the cabbage.
How can the farmer bring the wolf, the goat, and the cabbage across the river?

Breadth-first search is used to find the shortest path to the solution.
Every state neighbor is checked to see if it's valid, and if it is, it's added to the queue
Every item in the queue is visited until the goal state is reached
Since the queue is a FIFO, the first path to reach the goal state is the shortest one
"""

import json
from queue import Queue

# State is represented as {"farmer": False, "goat": False, "cabbage": False, "wolf": False}
# G - Goat
# C - Cabbage
# W - Wolf
# F - Farmer
# False - Left side


def hash_state(state):
    """
    Hash the state
    """
    return json.dumps(state)


def valid_state(state):
    """
    Check if the state is valid
    """
    if state["G"] == state["C"] and state["F"] != state["G"]:
        return False
    if state["G"] == state["W"] and state["F"] != state["G"]:
        return False

    return True


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


def state_as_string(state):
    """
    Convert the state to a FGWC|---- format
    """
    left_side = ""
    right_side = ""
    for key in state:
        if not state[key]:
            left_side += key
            right_side += "-"
        else:
            right_side += key
            left_side += "-"

    return f"{left_side}|{right_side}"


def wordify_path(path):
    """
    Convert the path to a human-readable format
    """
    string = [f"{state_as_string(path[0])} | Start"]
    for i in range(len(path) - 1):
        with_move = "alone"
        if path[i + 1]["G"] != path[i]["G"]:
            with_move = "with the goat"
        elif path[i + 1]["C"] != path[i]["C"]:
            with_move = "with the cabbage"
        elif path[i + 1]["W"] != path[i]["W"]:
            with_move = "with the wolf"

        move_dir = "right" if path[i + 1]["F"] else "left"
        string.append(
            f"{state_as_string(path[i+1])} | Farmer moves to the {move_dir} side {with_move}"
        )

    return string


# Initial state, all on the left side
starting_state = {"F": False, "G": False, "C": False, "W": False}

# Queue to store the states
q = Queue()
q.enqueue((starting_state, [starting_state]))

# Set to store the visited states
visited = set()
visited.add(hash_state(starting_state))

# Shortest path
shortest_path = None

# BFS
while not q.is_empty():
    # Get the current state and path
    current_state, path = q.dequeue()
    if (
        current_state["F"]
        and current_state["G"]
        and current_state["C"]
        and current_state["W"]
    ):
        # If the current state is the goal state, break
        shortest_path = path
        break
    for neighbor in get_neighbors(current_state):
        # For each neighbor, if it's not visited, add it to the queue and mark it as visited
        if hash_state(neighbor) not in visited:
            q.enqueue((neighbor, path + [neighbor]))
            visited.add(hash_state(neighbor))

# Print the shortest path
print(json.dumps(shortest_path, indent=2))
# Print human-readable path
print("\n".join(wordify_path(shortest_path)))
