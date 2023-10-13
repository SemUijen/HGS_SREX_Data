import random


class IndexSampler:

    def __init__(self, list_length: int):
        self.list_1 = list(range(list_length))
        self.list_2 = list(range(list_length))
        self.list_3 = list(range(list_length))
        self.list_4 = list(range(list_length))
        self.list_5 = list(range(list_length))
        self.list_6 = list(range(list_length))
        self.list_7 = list(range(list_length))
        self.list_8 = list(range(list_length))
        self.list_9 = list(range(list_length))
    def sample_index(self):
        i1 = random.choice(self.list_1)
        self.list_1.remove(i1)

        i2 = random.choice(self.list_2)
        self.list_2.remove(i2)

        i3 = random.choice(self.list_3)
        self.list_3.remove(i3)

        i4 = random.choice(self.list_4)
        self.list_4.remove(i4)

        i5 = random.choice(self.list_5)
        self.list_5.remove(i5)

        i6 = random.choice(self.list_6)
        self.list_6.remove(i6)

        i7 = random.choice(self.list_7)
        self.list_7.remove(i7)

        i8 = random.choice(self.list_8)
        self.list_8.remove(i8)

        i9 = random.choice(self.list_9)
        self.list_9.remove(i9)

        return i1, i2, i3, i4, i5, i6, i7, i8, i9
