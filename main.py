# coding: utf-8
import argparse
from query_parser import Buffer

ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', required=True, help='Name of the source file')
ap.add_argument('-b', '--bsize', required=True, help='Size of the buffer')
args = vars(ap.parse_args())

def main():
    # Abre o arquivo somente para leitura
    a = open(args['file'], 'r')
    
    # Define o tamanho do buffer
    buffer_size = int(args['bsize'])
    
    # Gera um buffer do tamanho determinado com + 2 espaços
    # para os sentinelas 'eof'
    data = [None for i in range(2*buffer_size + 2)]
    data[buffer_size], data[-1]  = 'eof', 'eof'

    # Flag de checagem para o buffer
    nbuffer = 0

    while True:
        # Lê os próximos n caracteres oara o buffer
        tmp = a.read(buffer_size)
        
        # Para o loop caso o arquivo tenha terminado
        if tmp == '':
            break

        # Checagem da flag de buffer
        # 0 -> primeira metade
        # 1 -> segunda metade
        # Atribui os caracteres lidos do arquivo para o buffer
        if nbuffer == 0:   
            data[0:buffer_size] = tmp
            nbuffer = 1
        else:
            data[buffer_size + 1: -1] = tmp
            nbuffer = 0
        
        print(data)

if __name__ == "__main__":
    main()