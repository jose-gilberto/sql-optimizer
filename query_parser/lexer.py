
class Lexer:

    def __init__(self):
        self._automate = {}
        self._letters = []
        self._numbers = []

    def run(self):
        pass

    def lexical_error(self, char, state):
        # Checa se há uma transição para esse caractere e retorna
        # se houve erro na sintaxe ou não.
        if char in self._automate[state]:
            return False
        else:
            return True

    def bad_id(self):
        pass

    def classifier_char(self, char, state):
        # Caso o caractere lido seja um espaço ou quebra de linha
        # a leitura é classificada como blank.
        char = 'blank' if (char == ' ' or char == '\n') else char
        if char in self._automate[state]:
            return char
        elif char in self._letters and 'letter' in self._automate[state]:
            return 'letter'
        elif char in self._numbers and 'num' in self._automate[state]:
            return 'num'
        else:
            return 'other'