# Julia Sabelli
# Advent of Code 2023
# Day 15: Lens Library | Part 2

def hash_algorithm(step):
    current_value = 0
    for char in step:
        ascii_value = ord(char)
        current_value += ascii_value
        current_value *= 17
        current_value %= 256
    return current_value


def hashmap_procedure(filename):
    boxes = [{} for _ in range(256)]
    total_focusing_power = 0

    with open(filename, 'r') as file:
        steps = file.read().replace('\n', '').split(',')

    for step in steps:
        box_index = hash_algorithm(step.split('=')[0] if '=' in step else step.split('-')[0])
        box = boxes[box_index]

        if '=' in step:
            label, focal_length = step.split('=')
            focal_length = int(focal_length)
            box[label] = focal_length
        elif '-' in step:
            label = step.split('-')[0]
            if label in box:
                del box[label]

    for box_index, box in enumerate(boxes):
        for slot_index, (label, focal_length) in enumerate(box.items(), start=1):
            total_focusing_power += (box_index + 1) * slot_index * focal_length

    return total_focusing_power


print(hashmap_procedure('../Part 1/input.txt'))
