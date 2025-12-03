class YAMLParser:
    def __init__(self, inp):
        self.inp = inp

    def skip_space(self):
        while len(self.inp) > 0 and self.inp[0]==' ':
            self.inp = self.inp[1:]

    def skip_newline(self):
        while len(self.inp) > 0 and self.inp[0]=='\n':
            self.inp = self.inp[1:]

    def parse_value(self, indent):
        self.skip_newline()
        self.skip_space()
        match self.inp[0]:
            case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
                return self.parse_number()
            case '"':
                return self.parse_string()
            case '-':
                return self.parse_array(indent)

        return self.parse_object(indent)

    def parse_number(self):
        number = []

        while len(self.inp) > 0 and self.inp[0] in "1234567890":
            number.append(self.inp[0])
            self.inp = self.inp[1:]

        if len(self.inp) > 0 and self.inp[0] == ".":
            number.append(self.inp[0])
            self.inp = self.inp[1:]

            while len(self.inp) > 0 and self.inp[0] in "1234567890":
                number.append(self.inp[0])
                self.inp = self.inp[1:]

        return float(''.join(number))

    def parse_string(self):
        string = ''
        self.inp = self.inp[1:]
        while len(self.inp) > 0 and self.inp[0] != '"':
            if self.inp[0] == "\\":
                self.inp = self.inp[1:]
                match self.inp[0]:
                    case 'n':
                        string += "\n"
                    case 't':
                        string +="\t"
                    case 'f':
                        string += "\f"
                    case 'b':
                        string += "\b"
                    case 'v':
                        string += "\v"
                    case 'r':
                        string += "\r"
                    case '\\':
                        string += "\\"
                    case '"':
                        string += '"'
                self.inp = self.inp[1:]
            else:
                string += self.inp[0]
                self.inp = self.inp[1:]
        self.inp = self.inp[1:]

        return string

    def parse_array(self, indent):
        array = []

        self.inp = self.inp[1:]
        self.skip_space()
        array.append(self.parse_value(indent + 1))
        self.skip_space()

        while self.inp.startswith("\n" + "  " * indent + '-'):
            self.skip_newline()
            self.skip_space()
            if len(self.inp) == 0:
                break
            self.inp = self.inp[1:]
            self.skip_space()
            array.append(self.parse_value(indent + 1))
            self.skip_space()
        return array

    def parse_object(self, indent):
        obj = {}

        name = ""
        while len(self.inp) > 0 and self.inp[0] != ':':
            name += self.inp[0]
            self.inp = self.inp[1:]
        self.inp = self.inp[1:]
        self.skip_space()
        obj[name] = self.parse_value(indent + 1)
        self.skip_space()

        while len(self.inp) > 0 and self.inp.startswith("\n" + "  " * indent):
            self.skip_newline()
            self.skip_space()
            name = ""
            if len(self.inp) == 0:
                break
            while len(self.inp) > 0 and self.inp[0] != ':':
                name += self.inp[0]
                self.inp = self.inp[1:]
            self.inp = self.inp[1:]
            self.skip_space()
            obj[name] = self.parse_value(indent + 1)
            self.skip_space()

        return obj