from Stack import *

maze = [
    ['+', '+', '+', '+', 'G', '+'],
    ['+', ' ', '+', ' ', ' ', '+'],
    ['+', ' ', ' ', ' ', '+', '+'],
    ['+', ' ', '+', '+', ' ', '+'],
    ['+', ' ', ' ', ' ', ' ', '+'],
    ['+', '+', '+', '+', '+', '+']]


def solveMaze(maze, startX, startY):
    stack = Stack()
    found = False
    count = 0
    pos = [startX, startY]
    stack.push(pos.copy())
    while not found:
        if maze[pos[0]][pos[1]] == 'G':
            found = True
        else:
            if maze[pos[0]][pos[1]] == ' ':
                count += 1
                maze[pos[0]][pos[1]] = count
            if maze[pos[0] - 1][pos[1]] == ' ' or maze[pos[0] - 1][pos[1]] == 'G':
                pos[0] -= 1
                stack.push(pos.copy())
                continue
            elif maze[pos[0]][pos[1] - 1] == ' ' or maze[pos[0]][pos[1] - 1] == 'G':
                pos[1] -= 1
                stack.push(pos.copy())
                continue
            elif maze[pos[0] + 1][pos[1]] == ' ' or maze[pos[0] + 1][pos[1]] == 'G':
                pos[0] += 1
                stack.push(pos.copy())
                continue
            elif maze[pos[0]][pos[1] + 1] == ' ' or maze[pos[0]][pos[1] + 1] == 'G':
                pos[1] += 1
                stack.push(pos.copy())
                continue
            else:
                #print("going back")
                stack.pop()
                if not stack.isEmpty():
                    pos = stack.peek().copy()
                elif stack.isEmpty() and count != 0:
                    return False
    return True


def printMaze(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            print("|{:<2}".format(maze[row][col]), sep='', end='')
        print("|")
    return

#solveMaze(maze, 4, 4)
#printMaze(maze)
