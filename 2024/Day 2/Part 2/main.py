def is_safe_report(levels):
  n = len(levels)

  if n < 2:
      return True  # A report with less than 2 levels is trivially safe

  increasing = all(levels[i] < levels[i+1] and 1 <= levels[i+1] - levels[i] <= 3 for i in range(n - 1))
  decreasing = all(levels[i] > levels[i+1] and 1 <= levels[i] - levels[i+1] <= 3 for i in range(n - 1))

  return increasing or decreasing

def can_be_safe_with_one_removal(levels):
  n = len(levels)
  for i in range(n):
      if is_safe_report(levels[:i] + levels[i+1:]):
          return True
  return False

def count_safe_reports(data):
  reports = data.strip().split('\n')
  safe_count = 0
  for report in reports:
      levels = list(map(int, report.split()))
      if is_safe_report(levels) or can_be_safe_with_one_removal(levels):
          safe_count += 1
  return safe_count

def result():
  with open("2.txt") as f:
      return f.read()

data = result()
print(count_safe_reports(data))