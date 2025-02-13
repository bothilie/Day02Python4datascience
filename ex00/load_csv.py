import pandas

#print l'ouput dans la fonction?

def load(path: str) -> []:
    try:
        data = pandas.read_csv(path)
        nb_col = data[data.columns[0]].count()
        nb_col = data.shape[0]
        nb_rows = data.shape[1]
        output = f"Loading dataset of dimensions ({nb_col},{nb_rows})"
        print(output)
        return(data)
    except:
        AssertionError("")
        return(None)