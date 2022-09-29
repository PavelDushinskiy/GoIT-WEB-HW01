class Meta(type):

    counter = 0

    def __new__(mcs, class_name, parents, attributes):
        class_number: type = type(class_name, parents, attributes)
        attributes['class_number'] = Meta.counter
        Meta.counter += 1
        return type(class_name, parents, attributes)


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


if __name__ == '__main__':
    print(Cls1.class_number, Cls2.class_number)
    assert (Cls1.class_number, Cls2.class_number) == (0, 1)
    a, b = Cls1(''), Cls2('')
    print(a.class_number, b.class_number)
    assert (a.class_number, b.class_number) == (0, 1)
