
class SymbolTable:

    def __init__(self):
        self._lastid = 0
        self._table = {}

    def add(self, name, attr = {}):
        id = self._lastid + 1
        self._table[id] = {
            'name': name,
            'attrs': attr
        }
        self._lastid = id
        return id

    def get_table(self):
        return self._table

