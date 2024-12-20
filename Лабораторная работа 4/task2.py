import csv
import json


def task(in_filename, out_filename) -> None:
    list_ = []
    with open(in_filename, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            list_.append(row)
        with open(out_filename, 'w', encoding='utf-8') as out:
            json.dump(list_, out, indent=4, ensure_ascii=False)


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

