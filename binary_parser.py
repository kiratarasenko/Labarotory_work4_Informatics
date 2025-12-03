
class BINARY_parser:
    def __init__(self, inp):
        self.inp = inp

    def parse_value(self):
        match self.inp[0]:
            case 1:
                return self.parse_number()
            case 2:
                return self.parse_string()
            case 3:
                return self.parse_array()
            case 4:
                return self.parse_object()
        return None

    def parse_number(self):
        if self.inp[0] == 1:
            self.inp = self.inp[1:]
            a,b,c,d=self.inp[:4]
            self.inp=self.inp[4:]
            number = a + (b << 8) + (c << 16) + (d << 24)
            return number

    def parse_string(self):
        if self.inp[0] == 2:
            string = ""
            self.inp = self.inp[1:]
            a, b, c, d = self.inp[:4]
            self.inp = self.inp[4:]
            len = a + (b << 8) + (c << 16) + (d << 24)
            string += self.inp[:len].decode("utf8")
            self.inp=self.inp[len:]
            return string

    def parse_array(self):
        if self.inp[0] == 3:
            self.inp = self.inp[1:]
            a, b, c, d = self.inp[:4]
            self.inp = self.inp[4:]
            array =[]
            len = a + (b << 8) + (c << 16) + (d << 24)
            for i in range(len):
                array.append(self.parse_value())
            return array


    def parse_object(self):
        if self.inp[0] == 4:
            self.inp = self.inp[1:]
            a, b, c, d = self.inp[:4]
            self.inp = self.inp[4:]
            len = a + (b << 8) + (c << 16) + (d << 24)
            obj = {}
            for i in range(len):
                key = self.parse_string()

                obj[key] = self.parse_value()

            return obj
        return None





