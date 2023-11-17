import math
from bitarray import bitarray

class BloomFilter(object):
    def __init__(self, size, number_expected_elements=100):
        #размер фильтра Блума
        self.size = size
        #кол-во ожидаемых элементов, которые хранит фильтр Блума
        self.number_expected_elements = number_expected_elements
        #массив из битов
        self.filter = bitarray(self.size)
        #заполнение массива из битов 0
        self.filter.setall(0)
        self.number_hash_functions = round((self.size / self.number_expected_elements) * math.log(2))

    def _hash_djb2(self, s):
        hash = 5381
        for x in s:
            hash = ((hash << 5) + hash) + ord(x)
        return hash % self.size

    def add_to_filter(self, item):
        for i in range(self.number_hash_functions):
            self.filter[self._hash_djb2(str(i) + item)] = 1

    def check_is_not_in_filter(self, item):
        for i in range(self.number_hash_functions):
            if self.filter[self._hash_djb2(str(i) + item)] == 0:
                return True
        return False