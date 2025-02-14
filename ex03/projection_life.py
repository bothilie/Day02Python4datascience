import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from load_csv import load

#quelle échelle ?
#quand se fait la conversion?

def convert_to_numeric(val):
    if val == 'str':
        val = val.upper().replace('M', 'e6').replace('K', 'e3')  # Replace suffixes
    return pd.to_numeric(val, errors='coerce')

def projection_life():
    projection_life.__doc__ = "it project the correlation between gdp and life expectancy"
    data_pop = load("life_expectancy_years.csv")
    data_gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    data_pop = data_pop.set_index('country')
    data_gdp = data_gdp.set_index('country')
    plt.scatter(data_gdp['1900'], data_pop['1900'])
    plt.title('1900')
    plt.ylabel('Life Expectancy')
    plt.xlabel('Gross domestic product')

    plt.show()

if __name__ == "__main__":
    projection_life()

