#!/usr/bin/env python

import fire

def greet(greeting='Hiya', name='Joe'):
    print(f'{greeting} {name}')

def goodbye(goodbye='Bye', name='Joe'):
    print(f'{goodbye} {name}')

if __name__ == '__main__':
    fire.Fire()
