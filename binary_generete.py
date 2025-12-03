"""
number=1 4 байт
string=2 len-4 байт len байт
array=3 len-4 байт-Элементов х-байт
object=4 len-4 ,байт-Ключи байт-Значения
"""
class binary_generate:
    def __init__(self, inp):
        self.inp = inp

    def object_bytes(self, inp):
        if type(inp) == int:
            array = [1, inp & 255, inp >> 8 & 255, inp >> 16 & 255, inp >> 24 & 255]
            return bytes(array)
        if type(inp) == str:
            byte = bytes(inp, "utf-8")
            array = [2, len(byte) & 255, len(byte) >> 8 & 255, len(byte) >> 16 & 255, len(byte) >> 24 & 255 ]
            return bytes(array) + byte
        if type(inp) == list:
            array = bytes([3, len(inp) & 255, len(inp) >> 8 & 255, len(inp) >> 16 & 255, len(inp) >> 24 & 255])
            for i in inp:
                array += self.object_bytes(i)
            return array
        if type(inp) == dict:
            array = bytes([4, len(inp) & 255, len(inp) >> 8 & 255, len(inp) >> 16 & 255, len(inp) >> 24 & 255])
            for key, value in inp.items():
                array += self.object_bytes(key)+ self.object_bytes(value)
            return array
        return None


