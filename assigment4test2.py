maze_list = []
with open("maze.txt", "r") as maze_map:
    for line in maze_map:
        temp_list = list(line.strip())
        maze_list.append(temp_list)

start_index = (4,0)

up = 0
right = 1
down = 2
left = 3

def wall_check(direction, location):
    if direction == 0:
        if maze_list[location[0]][location[1]+1] == "W":
            return True
    elif direction == 1:
        if maze_list[location[0]-1][location[1]] == "W":
            return True
    elif direction == 2:
        if maze_list[location[0]][location[1]-1] == "W":
            return True
    elif direction == 3:
         if maze_list[location[0]+1][location[1]] == "W":
            return True
    else:
        return False


def maze_solver(direction, location):
    if location == "S":
        return True
    else:
        if direction == 0:
            if maze_list[location[0]][location[1]+1] == "W":
                maze_list[location[0]-1][location[1]] = "V"
                return maze_solver(direction, (location[0]-1, location[1]))
        elif direction == 1:
            if maze_list[location[0]-1][location[1]] == "W":
                maze_list[location[0]-1][location[1]] = "V"
                return maze_solver(direction, (location[0], location[1]+1))
        elif direction == 2:
            if maze_list[location[0]][location[1]-1] == "W":
                maze_list[location[0]][location[1]-1] = "V"
                return maze_solver(direction, (location[0]))
        elif direction == 3:
            if maze_list[location[0]+1][location[1]] == "W":
                maze_list[location[0]+1][location[1]] = "V"
                return

for i in maze_list:
    print(i)

print("\n\n")
maze_solver(up, start_index)

for i in maze_list:
    print(i)

# Iflerin altına else ekle direk sağa gitsinler.
