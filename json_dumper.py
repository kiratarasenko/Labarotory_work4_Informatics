def json_con(obj):
    if type(obj) == int:
        number = str(obj)
        return number
    if type(obj) == str:
        obj = '"' + obj + '"'
        return obj
    if type(obj) == list:
        result = ""

        result += "["
        result += ",".join(map(json_con, obj))+"]"
        return result
    if type(obj) == dict:
        result = "{"
        for k, v in obj.items():
            result += '"' + k + '"' + ":" + json_con(v) + ",\n"

        result = result[:-2]
        result += "}"
        return result





