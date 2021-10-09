#!/usr/bin/env python
"""
Command-line tool using argparse
"""
import argparse

def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is setting sail")

def list_ships():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {','.join(ships)}")

def greet(greeting, name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Maritime control') 
    subparser = parser.add_subparsers(dest='func')
    ship_parser = subparser.add_parser('ships' , help="Ship related commands")
    ship_parser.add_argument('command' , choices= ['list', 'sail'])
    sail_parser = subparser.add_parser('sailors' , help="Talk to sailors")
    sail_parser.add_argument("Name" , help="SAilor name")
    sail_parser.add_argument('--greeting' , '-g' , help="Greeting" , default="Hello there")
    args = parser.parse_args()
    if args.func == 'sailors':
        greet(args.greeting,args.Name)
    elif args.command == 'list':
        list_ships()
    else:
        sail()
        
        
