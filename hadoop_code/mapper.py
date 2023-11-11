import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    nodeID, neighbours = line.strip().split(":")
    neighbours = neighbours.split(",")
    for i in range(len(neighbours)):
        if neighbours[i] == '1':
            print(f"{nodeID} {1}")
            #print(f'{word} {1}')

