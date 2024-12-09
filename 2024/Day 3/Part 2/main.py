import re

def extract_and_sum_multiplications(memory):
    # Regular expressions to find all valid mul(X,Y), do(), and don't() patterns
    mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")

    # Split the memory into tokens
    tokens = re.split(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))', memory)
    tokens = [token for token in tokens if token]  # Remove empty tokens

    # Perform the multiplications and sum the results
    total_sum = 0
    enabled = True  # Initially, mul instructions are enabled

    for token in tokens:
        if do_pattern.match(token):
            enabled = True
        elif dont_pattern.match(token):
            enabled = False
        elif mul_pattern.match(token):
            if enabled:
                x, y = mul_pattern.findall(token)[0]
                total_sum += int(x) * int(y)

    return total_sum

def data():
    with open("3.txt") as f:
        return f.read()

memory = data()

# Calculate the sum of the multiplications
result = extract_and_sum_multiplications(memory)
print(result)  # Output should be the sum of the enabled multiplications