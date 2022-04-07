def identity(value):
    return value


class Seen(list):
    def __bool__(self):
        return True

    def __call__(self, element):
        self.append(element)
