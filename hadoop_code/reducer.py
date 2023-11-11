import sys

current_node = None
current_count = 0
node = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    node, count = line.split()

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_node == node:
        current_count += count
    else:
        if current_node:
            # write result to STDOUT
            print(f'{current_node} {current_count}')
        current_count = count
        current_node = node

print(f'{current_node} {current_count}')

