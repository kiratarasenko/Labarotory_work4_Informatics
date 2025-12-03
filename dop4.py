from yaml_parser import YAMLParser
import binary_generete
from binary_parser import BINARY_parser
import json_dumper
import datetime
import yaml
import pickle
import json

start = datetime.datetime.now()

for _ in range(100):
    with open('schedule.yaml', 'r', encoding='utf-8') as file:
        yaml_text = file.read()

    parser_yaml = YAMLParser(yaml_text)
    data = parser_yaml.parse_value(0)
    binary_encoder = binary_generete.binary_generate(data)
    binary_data = binary_encoder.object_bytes(data)

    # записываем в бинарный файл
    with open("schedule1.bin", "wb") as my_file:
        my_file.write(binary_data)

    with open('schedule1.bin', 'rb') as file:
        binary_text = file.read()

    binary_parser = BINARY_parser(binary_text)
    data = binary_parser.parse_value()
    json_text = json_dumper.json_con(data)

    # записываем в json
    with open("schedule2.json", "w", encoding='utf-8') as my_file:
        my_file.write(json_text)

first = datetime.datetime.now()

for _ in range(100):
    with open("schedule.yaml", "r", encoding='utf-8') as my_file:
        schedule = yaml.load(my_file, Loader=yaml.FullLoader)

    with open("schedule_lab.bin", "wb") as f:
        pickle.dump(schedule, f, protocol=pickle.HIGHEST_PROTOCOL)

    with open("schedule_lab.bin", "rb") as f:
        schedule_lab1 = pickle.load(f)

    with open("schedule_lab.json", "w", encoding='utf-8') as fi:
        json.dump(schedule_lab1, fi, ensure_ascii=False)

second = datetime.datetime.now()

print(first - start)
print(second - first)
