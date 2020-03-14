
class Iterator:

    def __init__(self):
        pass

    def set_array(self, arr):
        self._array = arr
        self._f = 0
        self._lb = 0

    def get_character(self):
        return self._array[self._f]

    def first_lexem_char(self):
        return self._array[self._lb]

    def forward(self):
        return self._array[self._f + 1]
    
    def go_next(self):
        self._f += 1

    def go_back(self):
        self._f -= 1

    def lb_next(self):
        self._lb += 1
        self._f = self._lb

    def next_lexem(self):
        self._lb = self._f
        