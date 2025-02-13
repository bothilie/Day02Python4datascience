import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from load_csv import load

#automatiser l'indexation
#automatiser le pays
#tester

def aff_life():
    data = pd.read_csv("life_expectancy_years.csv")
    data = data.set_index("country")
    print(data[data.index == 'France'])
    data_fr = data[data.index == 'France'].squeeze()

    dfxy = pd.DataFrame(
    data={
        "life_expectancy": data_fr.values,},
    index=[1800 + i for i in range(0, 301)])
    dfxy.ylabel = "life expectancy"
    dfxy.plot(title="life expectancy in France between 1800 and 2101",
    figsize=(8, 6),
    fontsize=16,
    xlim=(1800, 2101))

    plt.show()

if __name__ == "__main__":
    aff_life()