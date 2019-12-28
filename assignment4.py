import sys


# All location tuples are in (x,y) format.
def maze_file_handling(maze_temp, maze_file):
    """Opens maze_file creates a list of lists with this file.
    Returns start location and H's locations list if H exists."""
    with open(maze_file, "r") as maze_map:
        for line in maze_map:
            temp_list = list(line.strip())
            maze_temp.append(temp_list)
    start_index = (0, 0)
    H_list = []
    for i in maze_temp:
        if "S" in i:
            start_index = (maze_temp.index(i), i.index("S"))
        if "H" in i:
            H_list.append((maze_temp.index(i), i.index("H")))
    return start_index, H_list


def look_around(maze, x):
    """ A helper function for maze_solver.
    Returns a dictionary as {left:letter, up:letter, right:letter, down:letter} addresses are (x,y) """
    around = dict()
    if x[1] > 0:  # left
        around[(x[0], x[1]-1)] = maze[x[0]][x[1]-1]
    if x[0] > 0:  # up
        around[(x[0]-1, x[1])] = maze[x[0]-1][x[1]]
    if x[1] + 1 < len(maze[0]):  # right
        around[(x[0], x[1]+1)] = maze[x[0]][x[1]+1]
    if x[0] + 1 < len(maze):  # down
        around[(x[0]+1, x[1])] = maze[x[0]+1][x[1]]
    return around


def maze_solver(start, maze, end):
    """Starts from start, solves maze recursively until end.
    Returns location of end, it can be H or F"""
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
    for i in range(H_counter):  # Solve maze for H time.
        start_index = maze_solver(start_index, maze, "H")
        T_counter_old = T_counter
        T_counter = 0
        for j in maze:
            T_counter += j.count("T")
        if T_counter - T_counter_old > health_time:  # Find number of steps and compare with health.
            return False
    maze_solver(start_index, maze, "F")  # Solve maze from last H to F
    T_counter_old = T_counter
    T_counter = 0
    for j in maze:
        T_counter += j.count("T")
    if T_counter - T_counter_old > health_time:  # Check health for last time.
        return False
    else:
        return True


def maze_printer(start_index, maze, H_location_list=None):
    """Transforms maze units to 1, 0, S and H, returns transformed maze."""
    for i in maze:
        for j in range(len(i)):
            if i[j] == "T":
                i[j] = 1
            if i[j] == "P" or i[j] == "W" or i[j] == "D":
                i[j] = 0
    if H_location_list is not None:
        for i in H_location_list:
            maze[i[0]][i[1]] = "H"
    maze[start_index[0]][start_index[1]] = "S"
    return maze


def main_solver(maze_file, maze_health_file, health_time, output_file):
    # Solve maze without health condition.
    maze_list = []
    start_index = maze_file_handling(maze_list, maze_file)[0]
    maze_solver(start_index, maze_list, "F")
    maze_result = maze_printer(start_index, maze_list)
    # Write first maze's solution to the output file.
    output = open(output_file, "w")
    output.write("Maze solution without health condition\n\n")
    for k in maze_result:
        output.write(','.join(map(str, k))+"\n")
    output.write("\nMaze solution with health condition\n\n")
    # Solve maze with health condition.
    maze_list = []
    start_index, H_location_list = maze_file_handling(maze_list, maze_health_file)
    health_result = with_health(start_index, maze_list, health_time)
    # Write second maze's solution to the output file.
    if health_result:
        maze_result = maze_printer(start_index, maze_list, H_location_list)
        for k in maze_result:
            output.write(','.join(map(str, k))+"\n")
    else:
        output.write("You have died.")


main_solver(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4])
