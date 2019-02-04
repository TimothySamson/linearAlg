class Test:
    def __init__(self, array):
        self.array = array

    def __getitem__(self, index):
        print(index)
        return self.array[index]

Test([1, 2, 3])[1]
