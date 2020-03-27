# coding: utf-8
import argparse
from query_parser import Buffer
from query_parser import SymbolTable
from query_parser import automate_dict
from query_parser import numbers
from query_parser import letters

ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', required=True, help='Name of the source file')
ap.add_argument('-b', '--bsize', required=True, help='Size of the buffer')
args = vars(ap.parse_args())


symbols_table = SymbolTable()
# automato[estado][entrada] -> retorna o próximo estado, se for -1
# state = automate_dict[state]['E']
# state = 2


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
                    token = '<' + \
                        automate_dict[state]['res'] + ', ' + lexem + '>'
                    tokens.append(token)
                elif automate_dict[state]['res'] == 'TXT':
                    token = '<' + \
                        automate_dict[state]['res'] + ', ' + lexem + '>'
                    tokens.append(token)
                elif automate_dict[state]['res'] == 'ID':
                    id = symbols_table.add(lexem)
                    token = '<' + \
                        automate_dict[state]['res'] + ', ' + str(id) + '>'
                    tokens.append(token)
                else:
                    tokens.append(automate_dict[state]['res'])
            elif 'outro' in automate_dict[state]:
                state = automate_dict[state]['outro']
                if automate_dict[state]['res'] == 'NUM':
                    token = '<' + \
                        automate_dict[state]['res'] + ', ' + lexem + '>'
                    tokens.append(token)
                elif automate_dict[state]['res'] == 'ID':
                    id = symbols_table.add(lexem)
                    token = '<' + \
                        automate_dict[state]['res'] + ', ' + str(id) + '>'
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
                    token = '<' + \
                        automate_dict[state]['res'] + ', ' + lexem + '>'
                    tokens.append(token)
                elif automate_dict[state]['res'] == 'TXT':
                    token = '<' + \
                        automate_dict[state]['res'] + ', ' + lexem + '>'
                    tokens.append(token)
                elif automate_dict[state]['res'] == 'ID':
                    id = symbols_table.add(lexem)
                    token = '<' + \
                        automate_dict[state]['res'] + ', ' + str(id) + '>'
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
                    print('\033[93m Debug - Char: {} - {} - {} \033[0m'.format(char,
                                                                               state, classifier_char(char, state)))
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
