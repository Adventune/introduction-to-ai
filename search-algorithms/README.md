# Search algorithms

Implementations of search algorithms taught during the course.

## Breadth- and depht-first searches

### Breadth-first search

[BFS](./bfs.py)

#### Hopefully senseful graphs

```mermaid
flowchart LR

    start_state --> 1_1 & 1_2 & 1_3
    1_1 --> 1
    1_2 --> 2
    1_3 --> 3

    next_state --> 2_1 & 2_2
    1 -- first item in queue popped to be next state --> next_state

    2_1 --> 4
    2_2 --> 5


    third_state --> 3_1
    2 -- second item in queue popped to be the next --> third_state

    3_1 --> 6


    subgraph queue
    QUEUE --> 1 --> 2 --> 3 --> 4 --> 5 --> 6
    end
```

Queue catches up with it's building (it's depth) once no more neighbors are found

```mermaid
flowchart TD

start_state --> 1_1 & 1_2 & 1_3

1_1 --> 2_1 & 2_2 & 2_3
1_2 --> 2_4 & 2_5 & 2_6
1_3 --> 2_7 & 2_8

2_1 --> 3_1 & 3_2 & 3_3
```

### Depth-first search

[DFS](./dfs.py)

#### Hopefully senseful graphs

```mermaid
flowchart LR

    start_state --> 1_1 & 1_2 & 1_3
    1_1 --> 1
    1_2 --> 2
    1_3 --> 3

    next_state --> 2_1 & 2_2
    3 -- last item in stack popped --> next_state

    2_1 --> 4
    2_2 --> 5


    third_state --> 3_1
    5 -- last item in stack popped --> third_state

    3_1 --> 6
    6 --starts backtracking when no more neighbors are found--> 4


    subgraph stack
    STACK --> 1 --> 2 --> 3 --> 4 --> 5 --> 6
    end

```

Stack starts backtracking and building it's breadth once no new neighbors for state are found

```mermaid
flowchart TD

start_state --> 1_1 & 1_2 & 1_3

1_1
1_2 --> 2_1 & 2_2 & 2_3
1_3 --> 2_4 & 2_5 & 2_6

2_6 --> 3_1 & 3_2 & 3_3
```
