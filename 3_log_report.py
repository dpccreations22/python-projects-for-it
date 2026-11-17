from collections import Counter

errors = Counter()
with open("app.log") as log:
    for line in log:
        if "ERROR" in line:
            ip = line.split()[2]
            errors[ip] += 1

print("Total errors:", sum(errors.values()))
for ip, count in errors.most_common(3):
    print(f"{ip:<16}{count}")
