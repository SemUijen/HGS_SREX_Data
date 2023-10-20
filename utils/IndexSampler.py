import random
from typing import List


class IndexSampler:

    def __init__(self, sample_list: List[int]):
        self.list_1 = sample_list

    def sample_index(self) -> int:
        i1 = random.choice(self.list_1)
        self.list_1.remove(i1)

        return i1
