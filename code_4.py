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
    #df.sort_index(axis=1).to_csv('sorted_report.csv', index = False)
    query_3 = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    year_result = df.query(query_3)
    min_query = year_result['dollar_price'].idxmin()
    cheapest_mac = round(year_result.loc[year_result]['dollar_price'],2)
    row = year_result[min_query]
    country = row['name']
    iso_a3 = row['iso_a3']
    sentence = f"{country}({iso_a3}): ${cheapest_mac}"
    return sentence

def get_the_most_expensive_big_mac_price_by_year(year):
    query_4 = f"(date>= '{year}-01-01' and )"

if __name__ == "__main__":
    pass