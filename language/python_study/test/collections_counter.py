from collections import Counter

data = [1, 2, 2, 3, 3, 3, 4, 4, 4]

counter = Counter(data)
max_count = max(counter.values())
modes = [key for key, count in counter.items() if count == max_count]

print(f"최빈값 목록: {modes}")