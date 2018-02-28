import pandas as pd

def readCSV(url):
    return pd.read_csv(url)

def addNewCol(data):
    #creating new dataframe with the additional column
    data['nameFull'] = data["nameFirst"] +" " + data ["nameLast"]
    return pd.DataFrame(data)



def writeCSV(df):
    f = open("fullname.csv","w")
    df = df[['nameFirst', 'nameLast','nameFull']]
    #writing dataframe to csv 
    df.to_csv(f,',','--')
    f.close()
    #print(df)

def main():
    url = "./baseballdatabank-master/core/Master.csv"
    data = readCSV(url)
    #print(data["nameFirst"] + " " + data["nameLast"])
    df =addNewCol(data)
    writeCSV(df)

main()

