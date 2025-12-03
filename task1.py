import yaml_parser
import binary_generete

with open('schedule.yaml', 'r', encoding='utf-8') as file:
    yaml_text = file.read()

yaml_parser = yaml_parser.YAMLParser(yaml_text)
data = yaml_parser.parse_value(0)
binary_encoder = binary_generete.binary_generate(data)
binary_data = binary_encoder.object_bytes(data)

# записываем в бинарный файл
with open("schedule1.bin", "wb") as my_file:
    my_file.write(binary_data)




