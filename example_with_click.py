#!/usr/bin/env python
import click
@click.group()
def cli():
    pass
@click.group(help="Ship related commands")
def ships():
    pass
cli.add_command(ships)
@ships.command(help="Sail a ship")
def sail():
    name_of_boat='Your boat'
    print(f'Name of boat: {name_of_boat}')
@ships.command(help="List all boats")
def list():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(','.join(ships))
@cli.command(help="Talk to a sailor")
@click.option('--greeting' , default="Ahoy" , help="Greet to sailor")
@click.argument('name')
def sailors(greeting,name):
    print(f'{greeting} , {name}')
if __name__=='__main__':
    cli()
    
    
    
