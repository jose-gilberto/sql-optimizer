
class SymbolTable:

    def __init__(self):
        self._lastid = 0
        self._table = {}

    def indexOf(self, name):
        for id in self._table:
            if self._table[id]['name'] == name:
                return id
        return -1

    def add(self, name, attr = {}):
        lastindex = self.indexOf(name)
        if lastindex == -1:
            id = self._lastid + 1
            self._table[id] = {
                'name': name,
                'attrs': attr
            }
            self._lastid = id
            return id
        return lastindex

    def get_table(self):
        return self._table

