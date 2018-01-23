import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version",
                action="version", default=argparse.SUPPRESS,
                version="%(prog)s (version " ")\n",
                help="show program's version number and exit")