from query_parser import Buffer
from .resources import automate_dict
from .resources import letters
from .resources import numbers


class Lexer:

    def __init__(self, symbol_table, buffer):
        self._symbol_table = symbol_table
        self._automate = automate_dict
        self._letters = letters
        self._numbers = numbers
        self._buffer = buffer
        self._tokens = []

    def run(self):
        nbuffer, state, line, col = 0, 0, 1, 0
        lexem = ''

        while True:
            flag = self._buffer.read()

            if flag == False:
                if self._automate[state]['final'] == True:
                    self.make_token(state, lexem)
                elif 'outro' in self._automate[state]:
                    state = self._automate[state]['outro']
                    if self._automate[state]['res'] == 'NUM':
                        token = '<' + \
                            self._automate[state]['res'] + ', ' + lexem + '>'
                        self._tokens.append(token)
                    elif self._automate[state]['res'] == 'ID':
                        id = self._symbol_table.add(lexem)
                        token = '<' + \
                            self._automate[state]['res'] + ', ' + str(id) + '>'
                        self._tokens.append(token)
                    else:
                        self._tokens.append(self._automate[state]['res'])
                break

            arr = self._buffer.get_buffer()
            nbuffer = 1 if nbuffer == 0 else 0
            i = 0

            while i < len(arr):
                char = arr[i]
                if self._automate[state]['final'] == True:
                    self.make_token(state, lexem)
                    if self._automate[state]['next'] == True:
                        i += 1
                    state = 0
                    lexem = ''
                else:
                    if char == 'eof':
                        i += 1
                    else:
                        if char == '\n':
                            line += 1

                        print('\033[93m Debug - Char: {} - {} - {} \033[0m'.format(char,
                                                                                   state, self.classifier_char(char, state)))

                        if self.classifier_char(char, state) not in self._automate[state]:
                            raise SyntaxError(
                                'Syntax error on line: {} in lexeme: {}'.format(line, lexem + char))

                        if state == 48 and self.classifier_char(char, state) == 'outro':
                            i += 1
                            lexem += char
                        elif self.classifier_char(char, state) != 'outro':
                            i += 1
                            if char != ' ':
                                lexem += char
                        state = self._automate[state][self.classifier_char(
                            char, state)]

            if flag == False:
                break

        return self._tokens

    def lexical_error(self, char, state):
        # Checa se há uma transição para esse caractere e retorna
        # se houve erro na sintaxe ou não.
        if char in self._automate[state]:
            return False
        else:
            return True

    def make_token(self, state, lexem):

        if self._automate[state]['res'] == 'NUM':
            token = '<' + \
                self._automate[state]['res'] + ', ' + lexem + '>'
            self._tokens.append(token)
        elif self._automate[state]['res'] == 'TXT':
            token = '<' + \
                self._automate[state]['res'] + ', ' + lexem + '>'
            self._tokens.append(token)
        elif self._automate[state]['res'] == 'ID':
            id = self._symbol_table.add(lexem)
            token = '<' + \
                self._automate[state]['res'] + ', ' + str(id) + '>'
            self._tokens.append(token)
        elif self._automate[state]['res'] == 'DATE':
            token = '<' +\
                self._automate[state]['res'] + ', ' + lexem + '>'
            self._tokens.append(token)
        else:
            self._tokens.append(self._automate[state]['res'])

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
            return 'outro'
