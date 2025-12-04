#!/usr/bin/env python3
from copy import deepcopy

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


def remove_accessible(grid):
    total = 0
    new_grid = deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1 and count_neighbors(grid, i, j)<4:
                total += 1
                new_grid[i][j]=0

    return new_grid, total
                

def main():
    input_file = "input.txt"
    total = 0
    removed = -1
    with open(input_file) as f:
        grid = parse_grid(f)
    while removed!=0:
        grid, removed = remove_accessible(grid)
        total += removed
        
    print(total)
    

if __name__ == '__main__':
    main()

