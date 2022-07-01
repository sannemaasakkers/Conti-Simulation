import argparse

parser = argparse.ArgumentParser(description="Create ContiLeaks demo website",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-n", "--name", help="Name of the hacked organisation")
parser.add_argument("-d", "--dir",  help="Directory of the stolen files")
args = parser.parse_args()
