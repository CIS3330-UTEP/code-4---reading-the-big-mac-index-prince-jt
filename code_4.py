import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv('./big-mac-full-index.csv')

#print(df)
#First 2 are queries
def get_big_mac_price_by_year(year,country_code):
     #date format: yyyy-mm-dd
    query_text = f"(date >= '{year}-01-01' and date <= '{year}-12-31 and iso_a3 == '{country_code.upper()}')"
    sub_df = df.query(query_text)
    mean_price = (round(sub_df['dollar_price'].mean(),2))
    return mean_price
    
    

def get_big_mac_price_by_country(country_code):
    query_2 = f"(iso_a3 == '{country_code.upper()}')"
    c_price = df.query(query_2)
    dollar_price = (round(c_price['dollar_price'].mean(),2))
    return dollar_price


#These two require indexes
def get_the_cheapest_big_mac_price_by_year(year):
    df.sort_index(axis=1).to_csv('sorted_report.csv', index = False)
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2018,"USA"))