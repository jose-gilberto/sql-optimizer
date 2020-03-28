import argparse
from query_parser import Buffer
from query_parser import Lexer
from query_parser import SymbolTable

ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', required=True, help='Name of the source file')
ap.add_argument('-b', '--bsize', required=True, help='Size of the buffer')
args = vars(ap.parse_args())

symbols_table = SymbolTable()

buffer_size = int(args['bsize'])
buffer = Buffer(buffer_size, args['file'])
buffer.open_file()

lexer = Lexer(symbols_table, buffer)
tokens = lexer.run()

print(tokens)
print(symbols_table.get_table())