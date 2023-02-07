import pandas as pd 
def read_csv(filename):
    df = pd.read_csv(filename)
    return df 
def write_csv(df, filename):
    df.to_csv(filename, index=True)
def add_element(df, element):
    df = df.append(element, ignore_index=True)
    return df 
def print_dataframe(df):
    print(df)

if __name__ == "__main__":
    filename = 'Data.csv'
   
    df = read_csv(filename)
    
    element = {'ID': '0', 'Name': 'Ivan', 'Last name': 'Shishkin', 'Age': 14, 'Height': 165, 'Weight': 52}
    element = {'ID': '1', 'Name': 'Konstantin', 'Last name': 'Simonov', 'Age': 15, 'Height': 175, 'Weight': 57}
    element = {'ID': '2', 'Name': 'Alexander', 'Last name': 'Morokin', 'Age': 30, 'Height': 191, 'Weight': 72}
    element = {'ID': '3', 'Name': 'Vadim', 'Last name': 'Medvedev', 'Age': 45, 'Height': 160, 'Weight': 95}
    df = add_element(df, element)
    
    print_dataframe(df)

    write_csv(df, filename)