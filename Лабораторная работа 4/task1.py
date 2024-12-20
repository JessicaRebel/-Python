import json
# TODO решите задачу


def task(filename) -> float:
    with open(filename) as f:
        data = json.load(f)
    s = 0
    for dictn in data:
        s += dictn["score"] * dictn["weight"]
    return round(s, 3)


print(task("input.json"))

