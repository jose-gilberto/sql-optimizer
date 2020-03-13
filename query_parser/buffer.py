
class Buffer:

    def __init__(self, bsize, filename):
        self._size = bsize
        self._filename = filename
        self._buffer = [None for i in range((self._size * 2) + 2)]
        self._buffer[self._size], self._buffer[-1] = 'eof', 'eof'
        self._nbuffer = 0

    def open_file(self):
        self._file = open(self._filename, 'r')

    def read(self):
        tmp = self._file.read(self._size)

        if tmp == '':
            return False

        if self._nbuffer == 0:
            self._buffer[0:self._size] = tmp
            self._nbuffer = 1
        else:
            self._buffer[self._size + 1: -1] = tmp
            self._nbuffer = 0
        
        return True

    def get_buffer(self):
        return self._buffer