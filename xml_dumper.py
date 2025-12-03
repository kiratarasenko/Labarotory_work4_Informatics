
def xml_con(obj):
    if type(obj) == int:
        number = f"""<number>{obj}</number>"""
        return number
    if type(obj) == str:
        for char in obj:
            if char == "<":
                char = "&lt"
            if char == ">":
                char = "&gt"
            if char == '"':
                char = "&quot"
            if char == "'":
                char = "&apos"
            if char == "&":
                char = "&amp"

        obj = f"<string>{obj}</string>"
        return obj
    if type(obj) == list:
        result = "<array>"
        for v in obj:
            result += xml_con(v)
        result += "</array>"
        return result
    if type(obj) == dict:
        result = "<object>"
        for k, v in obj.items():
            result += f'<key name="{k}">' + xml_con(v) + "</key>"
        result += "</object>"
        return result


import binary_parser

with open('schedule1.bin', 'rb') as file:
    binary_text = file.read()

binary_parser = binary_parser.BINARY_parser(binary_text)
data = binary_parser.parse_value()

xml = xml_con(data)

with open("schedule3.xml", "w", encoding='utf-8') as my_file:
    my_file.write(xml)
