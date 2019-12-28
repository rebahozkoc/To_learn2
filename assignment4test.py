import sys


def look_around(maze, x):
    """Returns a dictionary as {left:letter, up:letter, right:letter, down:letter} addresses are (x,y) """
    around = dict()
    if x[1] > 0:  # left
        around[(x[0], x[1]-1)]= maze[x[0]][x[1]-1]
    if x[0] > 0:  # up
        around[(x[0]-1, x[1])]= maze[x[0]-1][x[1]]
    if x[1] + 1 < len(maze[0]):  # right
        around[(x[0], x[1]+1)] = maze[x[0]][x[1]+1]
    if x[0] + 1 < len(maze):  # down
        around[(x[0]+1, x[1])] = maze[x[0]+1][x[1]]
    return around


def maze_solver(start, maze, end):
    look = look_around(maze, start)
    for i in look.keys():
        if look[i] == end:
            maze[start[0]][start[1]] = "T"
            return i
        if look[i] == "P":
            maze[start[0]][start[1]] = "T"
            return maze_solver(i, maze, end)
    for i in look.keys():
        if look[i] == "T":
            maze[start[0]][start[1]] = "D"  # Dead end
            return maze_solver(i, maze, end)


def with_health(start_index, maze, health_time):
    H_counter = 0
    T_counter = 0
    for i in maze:
            H_counter += i.count("H")
    for i in range(H_counter):
        start_index = maze_solver(start_index, maze, "H")
        T_counter_old = T_counter
        T_counter = 0
        for j in maze:
            T_counter += j.count("T")
        print("T_counter, T_counter_old", T_counter, T_counter_old)
        if T_counter - T_counter_old > health_time:
            print("You died")
            return False
    maze_solver(start_index, maze, "F")
    T_counter_old = T_counter
    T_counter = 0
    for j in maze:
            T_counter += j.count("T")
    if T_counter - T_counter_old > health_time:
        print("You died")
        return False
    else:
        return maze


def main_solver(maze_health_file,health_time):
    maze_list = []
    with open(maze_health_file, "r") as maze_map:
        for line in maze_map:
            temp_list = list(line.strip())
            maze_list.append(temp_list)
    start_index = (0, 0)
    for i in maze_list:
        if "S" in i:
            start_index = (maze_list.index(i), i.index("S"))
    health_result = with_health(start_index, maze_list, int(health_time))
    for i in maze_list:
        print(i)


main_solver(sys.argv[1], sys.argv[2])
