#!/usr/bin/python env
"""
Command-line tool using click
"""
import click

@click.group()
def cli():
    pass

@click.group(help='Ship level commands')
def ships():
    pass

cli.add_command(ships)

@ships.command(help='Sail a ship')
def sail():
    ship_name = 'Slice of Life'
    print(f'{ship_name} is setting sail...')

@ships.command(help='List all ships')
def list_ships():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {', '.join(ships)}")

@cli.command(help='Talk to a sailor')
@click.option('--greeting', default='Ahoy there', help='Greeting for sailor')
@click.argument('name')
def sailors(greeting, name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    cli()
