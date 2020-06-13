#!/usr/bin/env python

# Simple sys.argv command-line tool

import sys

def say_it(greeting, target):
    message = f'{greeting} {target}'
    print(message)

if __name__ == '__main__':
        greeting = 'Hello'
        target = 'Joe'

        if '--help' in sys.argv:
            help_msg = f'Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>'
            print(help_msg)
            sys.exit()

        if '--name' in sys.argv:
            name_index = sys.argv.index('--name') + 1
            if name_index < len(sys.argv):
                target = sys.argv[name_index]

        if '--greeting' in sys.argv:
            greeting_index = sys.argv.index('--greeting') + 1
            if greeting_index < len(sys.argv):
                greeting = sys.argv[greeting_index]

        say_it(greeting, target)
