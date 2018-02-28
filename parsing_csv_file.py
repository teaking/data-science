import os 
import itertools
import csv

DATADIR = ""
DATAFIlE = "./csv/beatles-discography.csv"

def parse_file(datafile):
    data = []
    with open(datafile, 'r') as f:
        read = csv.DictReader(f, delimiter=',')
        for line in read:
#only reading 10 line from the csv file
            if len(data) == 10: break 
            data.append(line)
    return data

def test():
#testing implementation 
    datafile = os.path.join(DATADIR, DATAFIlE)
    d = parse_file(datafile)

    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
    
    assert d[0] == firstline
    assert d[9] == tenthline

test()
