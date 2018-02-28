import pandas
import pandasql
#task - run sql query on a dataframe of weather data
#return - one column and one row - a count of the number of days in the dataframe where the rain column is equal to 1

#globals() DataFrame exists in global scope,
#locals() DataFrame is only defined inside a function and does not exists in global scope
def num_rainy_days(filename):
    weather_data = pandas.read_csv(filename)
    q = """
    select count(rain) as weather_data from weather_data where rain == 1;
    """
    rainy_days = pandasql.sqldf(q.lower(),locals())
    return rainy_days

def max_temp_aggregate_by_fog(filename):
    weather_data = pandas.read_csv(filename)
 #   , MAX(cast (maxtempi as integer)) 
    q = """
    select fog, MAX(cast(maxtempi as integer))from weather_data GROUP BY fog;
    """
    foggy_days =pandasql.sqldf(q.lower(),locals())
    return foggy_days

def avg_weekend_temp(filename):
    weather_data = pandas.read_csv(filename)
    q = """
    select AVG(cast(meantempi as integer))  from weather_data where cast(strftime('%w',date) as integer) = 6 or cast(strftime('%w',date) as integer) = 0;

    """
    avg_temp = pandasql.sqldf(q.lower(), locals())
    return avg_temp

def avg_min_temp(filename):
    weather_data = pandas.read_csv(filename)
    q = """
    SELECT AVG(cast(mintempi as intger)) FROM weather_data WHERE cast(rain as integer) == 1 and cast(mintempi as integer) > 55;
    """
    avg_min_temp_rainy = pandasql.sqldf(q.lower(),locals())
    return avg_min_temp_rainy


def main():
    filename = "./weather_underground.csv"
#    print(num_rainy_days(filename))   
#    print(max_temp_aggregate_by_fog(filename))
#    print(avg_weekend_temp(filename))
    print (avg_min_temp(filename))




main()
