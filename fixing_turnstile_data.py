import requests 
import pandas
import csv

def get_data():
    url = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt"
    req = requests.get(url)
    return req

def change_dataframe():
    d = pandas.read_csv("./mtr.csv")
    print('true' if isinstance(d, pandas.DataFrame) else 'false')
    d.fillna(0)
    print(list(d))
    print(d.index.values)
#create new dataframe to add edit data 

def write_dataframe_to_csv(retrieve_data):
    file_location = "./mtr.csv"
#dumping data retrieve from url to text file
    f = open(file_location, 'w')
    f.write(retrieve_data.text)
    f.close

    
def main():
   # write_dataframe_to_csv(get_data())
    f_in = open('./mtr.csv', 'r')
    f_out = open('./updated_mtr.csv', 'w')
    
    csv_read = csv.reader(f_in, delimiter = ',')

    csv_write = csv.writer(f_out, delimiter = ',')
    
    for line in csv_read:
        line_len = len(line)

        c1 = line[0]
        c2 = line[1]
        c3 = line[2]
        i = 3
        while i < len(line):
            line_update = [c1,c2,c3,line[i],line[i+1],line[i+2],line[i+3],line[i+4]]
            csv_write.writerow(line_update)
            i += 5

    f_in.close()
    f_out.close()




main()







