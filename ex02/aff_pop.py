import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from load_csv import load

#automatiser l'indexation
#automatiser le pays
#tester: quelles erreurs puisque c'est un pg ?
#PB FORMATTING GENERAL
#Modif xlim/ylim

def formatting(arr: []) -> []:
    new_arr= []
    for item in arr:
        if item.count("M"):
            item = item.rstrip(item[-1])
            item = float(item)*1000000
            print(item)
    print(arr)
    return(arr)

def convert_to_numeric(val):
    val = val.upper().replace('M', 'e6').replace('K', 'e3')  # Replace suffixes
    return pd.to_numeric(val, errors='coerce')


def aff_pop():
    aff_pop.__doc__="load a csv file and display a grap of the total population of France and belogium from 1800 to 2050"
    data = load("population_total.csv")
    if data.empty == True:
        print("No data")
        return(None)
    nb_rows = 250
    data = data.set_index("country")
    print(data[data.index == 'France'])
    data_fr = data[data.index == 'France'].squeeze()
    data_fr = data_fr[0:250]
    data_be = data[data.index == 'Belgium'].squeeze()
    data_be = data_be[0:250]
    data_fr = data_fr.apply(convert_to_numeric)
    data_be = data_be.apply(convert_to_numeric)
    lst = data_fr.index.to_list()
    print(len(lst))
    dfxy = pd.DataFrame(
    data={
        "total_population France": data_fr.values, 
        "total_population Belgium":data_be.values },
    #index = data_fr.index.values)
    index=[int(lst[0]) + i for i in range(0, len(data_fr))])
    dfxy.plot(title="Population projections",
    xlabel="Year",
    ylabel="Population",
    figsize=(8, 6),
    fontsize=16,)

    plt.show()

if __name__ == "__main__":
    aff_pop()