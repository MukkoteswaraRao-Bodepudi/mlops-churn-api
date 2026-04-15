import pandas as pd
def load_data(path):
    return pd.read_csv(path)

def preprocess(df):

    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors = 'coerce')

    df = df.dropna() # Dropping Missing or null values

    if 'customerID' in df.columns: #Dropping Customer Id Column
        df = df.drop('customerID', axis = 1)

    # one-hot encode categorical variables

    df = pd.get_dummies(df,drop_first = True)

    return df

if __name__ == '__main__':

    df = load_data("../data/churn.csv")

    df = preprocess(df)

    print(df.shape)
    
    print(df.head())

    print(df.columns)

    

    
