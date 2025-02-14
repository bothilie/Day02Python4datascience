import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from load_csv import load

#automatiser l'indexation
#automatiser le pays
#tester: quelles erreurs puisque c'est un pg ?

def aff_life():
    aff_life.__doc__="load a csv file and display a graph"
    data = load("life_expectancy_years1.csv")
    if data.empty == True:
        print("No data")
        return(None)
    nb_rows= data.shape[1]
    data = data.set_index("country")
    print(data[data.index == 'France'])
    data_fr = data[data.index == 'France'].squeeze()

    dfxy = pd.DataFrame(
    data={
        "life_expectancy": data_fr.values,},
    index=[1800 + i for i in range(0, nb_rows-1)])
    dfxy.ylabel = "life expectancy"
    dfxy.plot(title="France Life expectancy Projections",
    xlabel="Year",
    ylabel="life expectancy",
    figsize=(8, 6),
    fontsize=16,
    xlim=(1800, 1800+nb_rows))

    plt.show()

if __name__ == "__main__":
    aff_life()