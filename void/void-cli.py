import argparse

parser = argparse.ArgumentParser(description='stat converter for jiu jistics')

parser.add_argument('-iD', metavar='import directory', dest='import', type='str', help='The directory where your excel import files will be located')

args = parser.parse_args()

void = args