numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h',
           'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p',
           'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
           'Y', 'y', 'Z', 'z', '_'
           ]

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
        'num': 8,
        'outro': 9
    },
    2: {
        'final': False,
        'L': 3,
        'l': 3,
        'letter': 8,
        'num': 8,
        'outro': 9
    },
    3: {
        'final': False,
        'E': 4,
        'e': 4,
        'letter': 8,
        'num': 8,
        'outro': 9
    },
    4: {
        'final': False,
        'C': 5,
        'c': 5,
        'letter': 8,
        'num': 8,
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
        'letter': 8,
        'num': 8,
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
        'num': 8,
        'outro': 9
    },
    11: {
        'final': False,
        'O': 12,
        'o': 12,
        'letter': 8,
        'num': 8,
        'outro': 9
    },
    12: {
        'final': False,
        'M': 13,
        'm': 13,
        'letter': 8,
        'num': 8,
        'outro': 9
    },
    13: {
        'final': False,
        'outro': 14,
        'letter': 8,
        'num': 8,
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
        'num': 8,
        'outro': 9
    },
    16: {
        'final': False,
        'E': 17,
        'e': 17,
        'letter': 8,
        'num': 8,
        'outro': 9
    },
    17: {
        'final': False,
        'R': 18,
        'r': 18,
        'letter': 8,
        'num': 8,
        'outro': 9
    },
    18: {
        'final': False,
        'E': 19,
        'e': 19,
        'letter': 8,
        'num': 8,
        'outro': 9
    },
    19: {
        'final': False,
        'outro': 20,
        'letter': 8,
        'num': 8,
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
        'num': 8,
        'outro': 9
    },
    22: {
        'final': False,
        'D': 23,
        'd': 23,
        'letter': 8,
        'num': 8,
        'outro': 9
    },
    23: {
        'final': False,
        'outro': 24,
        'letter': 8,
        'num': 8,
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
        'num': 8,
        'outro': 9
    },
    26: {
        'final': False,
        'letter': 8,
        'num': 8,
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
        'num': 8,
        'outro': 9
    },
    29: {
        'final': False,
        'K': 30,
        'k': 30,
        'letter': 8,
        'num': 8,
        'outro': 9
    },
    30: {
        'final': False,
        'E': 31,
        'e': 31,
        'letter': 8,
        'num': 8,
        'outro': 9
    },
    31: {
        'final': False,
        'letter': 8,
        'num': 8,
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
        'num': 50,
        "'": 49
    },
    49: {
        'final': True,
        'res': 'TXT',
        'next': False
    },

    50: {
        'final': False,
        'outro': 48,
        'num': 51,
        "'": 49
    },
    51: {
        'final': False,
        'outro': 48,
        'num': 52,
        "'": 49
    },
    52: {
        'final': False,
        'outro': 48,
        'num': 53,
        "'": 49
    },

    53: {
        'final': False,
        'outro': 48,
        '-': 54,
        "'": 49
    },

    54: {
        'final': False,
        'outro': 48,
        'num': 55,
        "'": 49
    },
    55: {
        'final': False,
        'outro': 48,
        'num': 56,
        "'": 49
    },

    56: {
        'final': False,
        'outro': 48,
        '-': 57,
        "'": 49
    },

    57: {
        'final': False,
        'outro': 48,
        'num': 58,
        "'": 49
    },
    58: {
        'final': False,
        'outro': 48,
        'num': 59,
    },

    59: {
        'final': False,
        'outro': 48,
        "'": 60
    },
    60: {
        'final': True,
        'res': 'DATE',
        'next': False
    }
}
