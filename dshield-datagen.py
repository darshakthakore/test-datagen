import argparse
import requests

def main():

    # Get the file name from the command line that contains the raw data
    parser = argparse.ArgumentParser(description='Parse raw DShield data into DIS input format')
    parser.add_argument('--file', nargs='+', required=True, type=argparse.FileType('r'), help='file containing raw DShield data')

    args = parser.parse_args()
    infile = args.file[0]

    # Process each record
    for line in infile.readlines():
        if (line.strip())[0] != '#':
            processRecord(line.strip())

# Process each IP record by retrieving its metadata using the DShield API
def processRecord(record):
    # The IP address is the first one
    data = record.split()
    ip = data[0]


if __name__ == '__main__':
    main()




