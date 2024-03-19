"""
Copyright (c) 2024 Adventune. All Rights Reserved.
This file contains helper functions for the farmer, wolf, goat, and cabbage problem
"""

import json


def hash_state(state):
    """
    Hash the state into a string
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
