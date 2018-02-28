import os 

DATAFILE = "./csv/beatles-discography.csv"

def parse_file(datafile):
    data = []
    with open(datafile, "rb") as f:
        header = f.readline()#readline - read one entire line from the file
        header = header.decode().split(",")
        print(header)


parse_file(DATAFILE)

