class FlatIterator:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.out_counter = 0
        self.in_counter = -1
        return self

    def __next__(self):
        self.in_counter += 1
        if self.in_counter == len(self.n[self.out_counter]):
            self.out_counter += 1
            self.in_counter = 0
        if self.out_counter == len(self.n):
            raise StopIteration
        return self.n[self.out_counter][self.in_counter]


def test_1():

    list_of_lists_1 = [["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_1),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None],
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "h",
        False,
        1,
        2,
        None,
    ]


if __name__ == "__main__":
    test_1()
