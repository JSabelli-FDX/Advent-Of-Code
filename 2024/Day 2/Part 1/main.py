def is_safe_report(report):
  levels = list(map(int, report.split()))
  n = len(levels)

  if n < 2:
      return True  # A report with less than 2 levels is trivially safe

  increasing = all(levels[i] < levels[i+1] and 1 <= levels[i+1] - levels[i] <= 3 for i in range(n - 1))
  decreasing = all(levels[i] > levels[i+1] and 1 <= levels[i] - levels[i+1] <= 3 for i in range(n - 1))

  return increasing or decreasing

def result():
  with open("2.txt") as f:
      return f.read()

def count_safe_reports(data):
  reports = data.strip().split('\n')
  safe_count = sum(1 for report in reports if is_safe_report(report))
  return safe_count

data = result()
print(count_safe_reports(data))