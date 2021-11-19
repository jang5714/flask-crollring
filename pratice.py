class con(object):
    def data(self):
        some_dict = {'june': 12, 'hello': 22, 'world': 33}

        for i in some_dict.items():
            return print(type(i))


if __name__ == '__main__':
    c = con()
    # c.data()
    print(type(enumerate((1, 2))))
    print(type({'q': 1, 'b' : 2}.items()))

