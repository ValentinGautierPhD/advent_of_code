#!/usr/bin/env python3

def parse_grid(f):
    grid = []
    for l in f:
        row = []
        for caracter in l[:-1]:
            if caracter==".":
                row.append(0)
            elif caracter=="@":
                row.append(1)
        grid.append(row)
    return grid


def count_neighbors(grid, i, j):
    total = 0
    n,m = len(grid), len(grid[0])
    for k in range(-1,2):
        for l in range(-1,2):
            if (k,l)!=(0,0) and 0<=i+k<n and 0<=j+l<m:
                total += grid[i+k][j+l]
    return total

    
def main():
    input_file = "input.txt"
    total = 0
    with open(input_file) as f:
        grid = parse_grid(f)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1 and count_neighbors(grid, i, j)<4:
                total += 1
    print(total)
    

if __name__ == '__main__':
    main()
