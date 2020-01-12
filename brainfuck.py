#!usr/bin/python3
from math import sqrt
from sys import stdout, argv

class Refactor(object):
    def refactor(self, nr: int):
        root = int(sqrt(nr))
        return root, nr-(root**2)

class BrainFuck(object):
    """Converts a string into a BF program. Returns the BF code"""
    def text_to_brainfuck(self, data: str) -> 'brainfuck code':
        old = 0
        result = ''
        for character in data:
            _ord = ord(character)
            if old == _ord:
                stdout.write('.')
                continue

            deviation = _ord - old
            mult = Refactor().refactor(abs(deviation))
            if 0 < deviation: 
                if deviation < 6:
                    result += '{}.'.format('+'*deviation)
                else:
                    result += '>{}[<{}>-]<{}.'.format('+'*mult[0],'+'*mult[0],'+'*mult[1])
            else:
                if deviation > -6:
                    result += '{}.'.format('-'*abs(deviation))
                else:
                    result += '>{}[<{}>-]<{}.'.format('+'*mult[0],'-'*mult[0],'-'*mult[1])
            old = _ord
        return result

def help():
    stdout.write('-o --output filename   /save output data to filename with .bf extension\n\n')
    stdout.write('usage: brainfuck.py "your text here"')

if __name__ == '__main__':
    bf = BrainFuck()

    if len(argv) == 2:
        stdout.write(bf.text_to_brainfuck(argv[1]))
    elif len(argv) == 4:
        if argv[2] == '-o' or argv[2] == '--output':
            with open('{}.bf'.format(argv[3]), 'w') as file:
                file.write(bf.text_to_brainfuck(argv[1]))
        else: help()
    else: help()