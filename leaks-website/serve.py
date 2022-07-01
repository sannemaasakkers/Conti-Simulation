from bottle import route, run, template, static_file
import argparse
import os
import requests

parser = argparse.ArgumentParser(description="Create ContiLeaks demo website",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-n", "--name", help="Name of the hacked organisation", nargs="?", const="LeakedBV")
parser.add_argument("-d", "--dir",  help="Directory of the stolen files", nargs="?", const="demo")
parser.add_argument("-s", "--size", help="Amount of leaked files / file size", nargs="?", const="10GB")
args = parser.parse_args()

leaked_name = os.listdir(args.dir)[0]

@route('/<filename>.css')
def stylesheets(filename):
    return static_file('{}.css'.format(filename), root='css')

@route('/')
def conti():
    return template('index', organisation=args.name, leaked_size=args.size, leaked_name=leaked_name)

print("ContiLeaks page starting")

run(host='localhost', port=8000, debug=True)
