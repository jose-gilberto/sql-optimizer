# coding: utf-8
import argparse
from query_parser import Buffer
from query_parser import SymbolTable

ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', required=True, help='Name of the source file')
ap.add_argument('-b', '--bsize', required=True, help='Size of the buffer')
args = vars(ap.parse_args())

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h',
           'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p',
           'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
           'Y', 'y', 'Z', 'z', '_'
]

symbols_table = SymbolTable()
# automato[estado][entrada] -> retorna o próximo estado, se for -1
# state = automate_dict[state]['E']
# state = 2
automate_dict = {
    0: {
        'final': False,
        'blank': 0,
        '=': 33,
        's': 1,
        'S': 1,
        '<': 34,
        '>': 38,
        ',': 41,
        '.': 42,
        '*': 43,
        'num': 44,
        "'": 48,
        'letter': 8,
        'F': 10,
        'f': 10,
        'W': 15,
        'w': 15,
        'A': 21,
        'a': 21,
        'O': 25,
        'o': 25,
        'L': 28,
        'l': 28
    },
    1: {
        'final': False,
        'E': 2,
        'e': 2,
        'letter': 8,
        'outro': 9
    },
    2: {
        'final': False,
        'L': 3,
        'l': 3,
        'letter': 8,
        'outro': 9
    },
    3: {
        'final': False,
        'E': 4,
        'e': 4,
        'letter': 8,
        'outro': 9
    },
    4: {
        'final': False,
        'C': 5,
        'c': 5,
        'letter': 8,
        'outro': 9
    },
    5: {
        'final': False,
        'T': 6,
        't': 6,
        'letter': 8,
        'num': 8,
        'outro': 9
    },
    6: {
        'final': False,
        'outro': 7,
        'letter': 8
    },
    7: {
        'final': True,
        'res': 'SELECT',
        'next': False
    },
    8: {
        'final': False,
        'letter': 8,
        'num': 8,
        'outro': 9
    },
    9: {
        'final': True,
        'res': 'ID',
        'next': False
    },
    10: {
        'final': False,
        'R': 11,
        'r': 11,
        'letter': 8,
        'outro': 9
    },
    11: {
        'final': False,
        'O': 12,
        'o': 12,
        'letter': 8,
        'outro': 9
    },
    12: {
        'final': False,
        'M': 13,
        'm': 13,
        'letter': 8,
        'outro': 9
    },
    13: {
        'final': False,
        'outro': 14,
        'letter': 8
    },
    14: {
        'final': True,
        'res': 'FROM',
        'next': False
    },
    15: {
        'final': False,
        'H': 16,
        'h': 16,
        'letter': 8,
        'outro': 9
    },
    16: {
        'final': False,
        'E': 17,
        'e': 17,
        'letter': 8,
        'outro': 9
    },
    17: {
        'final': False,
        'R': 18,
        'r': 18,
        'letter': 8,
        'outro': 9
    },
    18: {
        'final': False,
        'E': 19,
        'e': 19,
        'letter': 8,
        'outro': 9
    },
    19: {
        'final': False,
        'outro': 20,
        'letter': 8
    },
    20: {
        'final': True,
        'res': 'WHERE',
        'next': False
    },
    21: {
        'final': False,
        'N': 22,
        'n': 22,
        'letter': 8,
        'outro': 9
    },
    22: {
        'final': False,
        'D': 23,
        'd': 23,
        'letter': 8,
        'outro': 9
    },
    23: {
        'final': False,
        'outro': 24,
        'letter': 8
    },
    24: {
        'final': True,
        'res': 'AND',
        'next': False
    },
    25: {
        'final': False,
        'R': 26,
        'r': 26,
        'letter': 8,
        'outro': 9
    },
    26: {
        'final': False,
        'letter': 8,
        'outro': 27
    },
    27: {
        'final': True,
        'res': 'OR',
        'next': False
    },
    28: {
        'final': False,
        'I': 29,
        'i': 29,
        'letter': 8,
        'outro': 9
    },
    29: {
        'final': False,
        'K': 30,
        'k': 30,
        'letter': 8,
        'outro': 9
    },
    30: {
        'final': False,
        'E': 31,
        'e': 31,
        'letter': 8,
        'outro': 9
    },
    31: {
        'final': False,
        'letter': 8,
        'outro': 32
    },
    32: {
        'final': True,
        'res': 'LIKE',
        'next': False
    },
    33: {
        'final': True,
        'res': '<EQ>',
        'next': False
    },
    34: {
        'final': False,
        'outro': 35,
        '=': 36,
        '>': 37
    },
    35: {
        'final': True,
        'res': '<LS>',
        'next': False
    },
    36: {
        'final': True,
        'res': '<LSE>',
        'next': True
    },
    37: {
        'final': True,
        'res': '<DIFF>',
        'next': True
    },
    38: {
        'final': False,
        '=': 39,
        'outro': 40
    },
    39: {
        'final': True,
        'res': '<GTE>',
        'next': True
    },
    40: {
        'final': True,
        'res': '<GT>',
        'next': False
    },
    41: {
        'final': True,
        'res': '<COMMA>',
        'next': False
    },
    42: {
        'final': True,
        'res': '<DOT>',
        'next': False
    },
    43: {
        'final': True,
        'res': '<MULT>',
        'next': False
    },
    44: {
        'final': False,
        'num': 44,
        'outro': 45,
        '.': 46
    },
    45: {
        'final': True,
        'res': 'NUM',
        'next': False
    },
    46: {
        'final': False,
        'num': 47
    },
    47: {
        'final': False,
        'num': 47,
        'outro': 45
    },
    48: {
        'final': False,
        'outro': 48,
        "'": 49
    },
    49: {
        'final': True,
        'res': 'TXT',
        'next': True
    }
}

def main():
    # Abre o arquivo somente para leitura
    # a = open(args['file'], 'r')
    count = 1
    # Define o tamanho do buffer
    buffer_size = int(args['bsize'])
    buffer = Buffer(buffer_size, args['file'])
    buffer.open_file()
    # Gera um buffer do tamanho determinado com + 2 espaços
    # para os sentinelas 'eof'
    # data = [None for i in range(2*buffer_size + 2)]
    # data[buffer_size], data[-1]  = 'eof', 'eof'

    # Flag de checagem para o buffer
    # nbuffer = 0

    state = 0
    tokens = []
    nbuffer = 0
    lexem = ''

    while True:
        # Lê os próximos n caracteres oara o buffer
        # tmp = a.read(buffer_size)
        flag = buffer.read()

        if flag == False:
            if automate_dict[state]['final'] == True:
                if automate_dict[state]['res'] == 'NUM':
                    token = '<' + automate_dict[state]['res'] + ', ' + lexem + '>'
                    tokens.append(token)
                elif automate_dict[state]['res'] == 'TXT':
                    token = '<' + automate_dict[state]['res'] + ', ' + lexem + '>'
                    tokens.append(token)
                elif automate_dict[state]['res'] == 'ID':
                    id = symbols_table.add(lexem)
                    token = '<' + automate_dict[state]['res'] + ', ' + str(id) + '>'
                    tokens.append(token)
                else:
                    tokens.append(automate_dict[state]['res'])
            elif 'outro' in automate_dict[state]:
                state = automate_dict[state]['outro']
                if automate_dict[state]['res'] == 'NUM':
                    token = '<' + automate_dict[state]['res'] + ', ' + lexem + '>'
                    tokens.append(token)
                elif automate_dict[state]['res'] == 'ID':
                    id = symbols_table.add(lexem)
                    token = '<' + automate_dict[state]['res'] + ', ' + str(id) + '>'
                    tokens.append(token)
                else:
                    tokens.append(automate_dict[state]['res'])
            break

        arr = buffer.get_buffer()
        # print(nbuffer)
        # print(arr)

        nbuffer = 1 if nbuffer == 0 else 0

        # Checagem da flag de buffer
        # 0 -> primeira metade
        # 1 -> segunda metade
        # Atribui os caracteres lidos do arquivo para o buffer
        # if nbuffer == 0:   
        #     data[0:buffer_size] = tmp
        #     nbuffer = 1
        # else:
        #     data[buffer_size + 1: -1] = tmp
        #     nbuffer = 0

        i = 0
        char = arr[i]
        
        while i < len(arr):
            char = arr[i]
            # print('Char: {} - State: {}'.format(char, state))

            if automate_dict[state]['final'] == True:
                if automate_dict[state]['res'] == 'NUM':
                    token = '<' + automate_dict[state]['res'] + ', ' + lexem + '>'
                    tokens.append(token)
                elif automate_dict[state]['res'] == 'TXT':
                    token = '<' + automate_dict[state]['res'] + ', ' + lexem + '>'
                    tokens.append(token)
                elif automate_dict[state]['res'] == 'ID':
                    id = symbols_table.add(lexem)
                    token = '<' + automate_dict[state]['res'] + ', ' + str(id) + '>'
                    tokens.append(token)
                else:
                    tokens.append(automate_dict[state]['res'])
                
                # print('Lexem: {} - Len: {}'.format(lexem, len(lexem)))

                # print(tokens)
                if automate_dict[state]['next'] == True:
                    i += 1
                state = 0
                lexem = ''
            else:
                if char == 'eof':
                    i += 1
                else:
                    print('\033[93m Debug - Char: {} - {} - {} \033[0m'.format(char, state, classifier_char(char, state)))
                    if state == 48 and classifier_char(char, state) == 'outro':
                        i += 1
                        lexem += char
                    elif classifier_char(char, state) != 'outro':
                        i += 1
                        if char != ' ':
                            lexem += char
                    state = automate_dict[state][classifier_char(char, state)]
                    

        # print(state)
        # print(arr)
        # print(buffer.eof_indexes())

        # Para o loop caso o arquivo tenha terminado
        if flag == False:
            break

    print(tokens)
    print(symbols_table.get_table())

def classifier_char(char, state):
    char = 'blank' if (char == ' ' or char == '\n') else char
    if char in automate_dict[state]:
        return char
    elif char in letters and 'letter' in automate_dict[state]:
        return 'letter'
    elif char in numbers and 'num' in automate_dict[state]:
        return 'num'
    else:
        return 'outro'

if __name__ == "__main__":
    main()