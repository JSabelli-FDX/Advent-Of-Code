def parse_disk_map(disk_map):
    blocks = []
    file_id = 0
    i = 0
    while i < len(disk_map):
        file_length = int(disk_map[i])
        blocks.extend([file_id] * file_length)
        i += 1
        if i < len(disk_map):
            free_space_length = int(disk_map[i])
            blocks.extend(['.'] * free_space_length)
            i += 1
        file_id += 1
    return blocks

def move_blocks_to_left(blocks):
    # Find the index of the leftmost '.' (free space) in the blocks list
    start_var = len(blocks) - 1
    # Iterate over the blocks list from the leftmost free space index to the end
    for i in range( len(blocks)):
        if blocks[i] == '.':
            while blocks[start_var] == '.':
                start_var -= 1

            if i > start_var:
                break

            blocks[i], blocks[start_var] = blocks[start_var], blocks[i]
    return blocks

def calculate_checksum(blocks):
    checksum = 0
    for position, block in enumerate(blocks):
        if block != '.':
            checksum += position * block
    return checksum

def main():
    with open("9.txt", "r") as file:
        disk_map = file.read().strip()

    blocks = parse_disk_map(disk_map)
    compacted_blocks = move_blocks_to_left(blocks)
    checksum = calculate_checksum(compacted_blocks)

    print("Filesystem checksum:", checksum)

if __name__ == "__main__":
    main()