#import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv('./big-mac-full-index.csv')

#print(df)
#First 2 are queries
def get_big_mac_price_by_year(year,country_code):
     #date format: yyyy-mm-dd
    query_text = f"(date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == '{country_code.upper()}')"
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
    min_index = year_result['dollar_price'].idxmin()
    cheapest_mac = round(year_result.loc[min_index]['dollar_price'],2)
    row = year_result.loc[min_index]
    country = row['name']
    iso_a3 = row['iso_a3']
    return f"{country}({iso_a3}): ${cheapest_mac}"


def get_the_most_expensive_big_mac_price_by_year(year):
    query_4 = f"(date >= '{year}-01-01' and date <= '{year}-12-31' )"
    year_result_2 = df.query(query_4)
    max_query = year_result_2['dollar_price'].idxmax()
    expensive = round(year_result_2.loc[max_query]['dollar_price'],2)
    row = year_result_2.loc[max_query]
    country = row['name']
    iso_a3 = row['iso_a3']
    sentence_expensive = f"{country}({iso_a3}): ${expensive}"
    return sentence_expensive

if __name__ == "__main__":
    year = 2003
    country_code = 'MYS'
    result_1 =get_big_mac_price_by_year(year,country_code)
    print(f"The price of a bigmac in {year}, location: {country_code} was ${result_1}.")

    result_2 = get_big_mac_price_by_country(country_code)
    print(f"The mean price of a bigmac was currently ${result_2}")

    result_3 = get_the_cheapest_big_mac_price_by_year(year)
    print(f"The cheapest bigmac in {year} was in {result_3}")

    result_4 = get_the_most_expensive_big_mac_price_by_year(year)
    print(f"The most expensive big mac in {year} was in {result_4}")

