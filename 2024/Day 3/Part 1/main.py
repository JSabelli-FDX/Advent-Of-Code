import re

def extract_and_sum_multiplications(memory):
    # Use regular expression to find all valid mul(X,Y) patterns
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    matches = pattern.findall(memory)

    # Perform the multiplications and sum the results
    total_sum = 0
    for x, y in matches:
        total_sum += int(x) * int(y)

    return total_sum

def data():
  with open("3.txt") as f:
      return f.read()

memory = data()

# Calculate the sum of the multiplications
result = extract_and_sum_multiplications(memory)
print(result)