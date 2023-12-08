# Julia Sabelli
# Advent of Code 2023
# Day 8: Haunted Wasteland | Part 1

def count_steps_to_destination(file_path, start='AAA', destination='ZZZ'):
    # Parse the input data
    with open(file_path, 'r') as file:
        lines = file.read().split('\n')
        instructions = lines[0]
        nodes = {line.split(' = ')[0]: tuple(line.split(' = ')[1][1:-1].split(', ')) for line in lines[1:] if ' = ' in line}

    # Initialize variables
    current_node = start
    steps = 0
    instruction_index = 0

    # Follow the instructions until we reach the destination
    while current_node != destination:
        # Get the next instruction
        instruction = instructions[instruction_index]

        # Update the current node based on the instruction
        current_node = nodes[current_node][0] if instruction == 'L' else nodes[current_node][1]

        # Update the steps count and the instruction index
        steps += 1
        instruction_index = (instruction_index + 1) % len(instructions)

    return steps


# Call the function with the path to the input file
print(count_steps_to_destination('input.txt'))
