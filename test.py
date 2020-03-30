import argparse
import pprint
import json
import os
from query_parser import Buffer
from query_parser import Lexer
from query_parser import SymbolTable

ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', required=True, help='Name of the source file')
ap.add_argument('-b', '--bsize', required=True, help='Size of the buffer')
args = vars(ap.parse_args())

symbol_table = SymbolTable()

buffer_size = int(args['bsize'])
buffer = Buffer(buffer_size, args['file'])
buffer.open_file()

lexer = Lexer(symbol_table, buffer)
tokens = lexer.run()

print('\nToken List')
pprint.pprint(tokens)
print('\nSymbol Table')
pprint.pprint(symbol_table.get_table())

tokens_json = json.dumps(tokens)
tokens_file = open('tokens.json', 'w+')
tokens_file.write(tokens_json)
tokens_file.close()