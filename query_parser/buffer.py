
class Buffer:

    def __init__(self, bsize, filename):
        """ Cria uma instância de um buffer de tamanho n vazio.

        Keyword arguments:
        bsize -- Tamanho do buffer, o buffer real terá o dobro do tamanho para formar os pares.
        filename -- Caminho/Nome do arquivo a ser lido.
        """
        self._size = bsize
        self._filename = filename
        self._buffer = [None for i in range((self._size * 2) + 2)]
        # Marcação dos sentinelas
        self._buffer[self._size], self._buffer[-1] = 'eof', 'eof'
        # Flag para indicar o próximo buffer
        # Buffer atual = nbuffer - 1
        self._nbuffer = 0

    def open_file(self):
        """ Abre uma referência de memória para o arquivo sem trazê-lo todo para a memória.
        Armazena uma instância de file object para ser manipulada posteriormente.
        """
        self._file = open(self._filename, 'r')

    def read(self):
        """ Lê uma parte do arquivo e armazena no buffer, caso o arquivo tenha terminado retorna 
        False, caso contrário retorna True.
        """
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

    def eof_indexes(self):
        indexes = []
        for i in range(len(self._buffer)):
            if self._buffer[i] == 'eof':
                indexes.append(i)
        return indexes      

    def get_buffer(self):
        """ Retorna o buffer da flag como array. """
        eof_indexes = self.eof_indexes()
        if self._nbuffer == 1:
            return self._buffer[:eof_indexes[0] + 1]
        else:
            return self._buffer[eof_indexes[0] + 1:]