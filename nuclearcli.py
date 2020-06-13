#!/usr/bin/env python

from functools import wraps
from time import time
from numba import jit
import click

# Timing decorator to see runtime of my functions
def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        ts = time()
        result = f(*args, **kwargs)
        te = time()
        print(f'fun: {f.__name__}, args: [{args}, {kwargs}] took: {te-ts} sec')
        return result
    return wrapper

# Numba JIT Compiling
@timing
@jit(nopython=True)
def expmean_jit(real):

    val = real.mean() ** 2
    return val

@click.group()
def cli():
    pass

@cli.command()
def jit_test(jit):
    real = real_estate_array()
    if jit:
        click.echo(click.style('Running with JIT', fg='green'))
        expmean_jit(real)
    else:
        click.echo(click.style('Running NO JIT', fg='red'))
        expmean(real)
