import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from load_csv import load

#automatiser l'indexation
#automatiser le pays
#tester: quelles erreurs puisque c'est un pg ?
#PB FORMATTING GENERAL
#PB FORMATTING M/k

def formatting(arr: []) -> []:
    new_arr= []
    for item in arr:
        if item.count("M"):
            item = item.rstrip(item[-1])
            item = float(item)*1000000
            print(item)
    print(arr)
    return(arr)


def aff_pop():
    aff_pop.__doc__="load a csv file and display a grap of the total population of France and belogium from 1800 to 2050"
    data = load("population_total.csv")
    #print(data)
    if data.empty == True:
        print("No data")
        return(None)
    #nb_rows= data.shape[1]
    nb_rows = 250
    data = data.set_index("country")
    print(data[data.index == 'France'])
    data_fr = data[data.index == 'France'].squeeze()
    data_fr = data_fr[0:250]
    data_be = data[data.index == 'Belgium'].squeeze()
    data_be = data_be[0:250]
   # data_be = data_be.astype(float)
  #  data_fr = data_fr.astype(float)
    #data_be = formatting(data_be)
    print(data_be.values)
    dfxy = pd.DataFrame(
    data={
        "total_population France": data_fr.values, 
        "total_population Belgium":data_be.values},
    index=[1800 + i for i in range(0, 250)])
    dfxy.plot(title="Population projections",
    xlabel="Year",
    ylabel="Population",
    figsize=(8, 6),
    fontsize=16,
    xlim=(1800, 2050))

    plt.show()

if __name__ == "__main__":
    aff_pop()