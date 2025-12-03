import binary_parser
import json_dumper

with open('schedule1.bin', 'rb') as file:
    binary_text = file.read()

binary_parser = binary_parser.BINARY_parser(binary_text)
data = binary_parser.parse_value()
json_text = json_dumper.json_con(data)

# записываем в json
with open("schedule2.json", "w", encoding='utf-8') as my_file:
    my_file.write(json_text)