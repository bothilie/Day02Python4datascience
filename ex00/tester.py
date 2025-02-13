from load_csv import load

data = load("life_expectancy_years.csv")
print(data)

#bad path
data = load("life_expectancy_years1.csv")
print(data)

#bad format
data = load("landscape.jpg")
print(data)