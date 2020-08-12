#iterator class
class custom_iterator :
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return custom_iterator_iter(self.n)


#iterator class
class custom_iterator_iter :
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n :
            i = self.i
            self.i += i
            return i
        else :
            raise StopIteration()
