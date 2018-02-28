import pandas
import numpy 

def impuation(filename):
    #replacing NAs in a dataframe or series. Using 
    #fillna(value) 
    data = pandas.read_csv(filename)
    #replacing NAs with  average value (mean)of 'column' 

    data['column'] = data['column'].fillna(numpy.mean(data['column']))
    return data


