import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import requests

API = 'http://34.128.67.116:5000'

def get_df(url):
    response = requests.get(API+url)
    if response.status_code == 200:
        data = response.json()
        df = pd.read_json(data)
        return df
    else:
        print("Request gagal, status code:", response.status_code)

def frozenset_to_string(fset):
    elements = ', '.join(map(str, fset))
    return f"({elements})"

def index(products, min_support, min_confidence):
    df = get_df('/customers')
    products = ["Games Product", "Music Product", "Education Product", "Video Product", "Call Center", "Use MyApp"]
    X = df.copy()[products]

    transactions = list()
    for i in range(len(X)):
        x = X.iloc[i]

        product_used = list()
        for product_name, usage in zip(x.index, x):
            if usage == "Yes":
                product_used.append(product_name)
        transactions.append(product_used)

    encoder = TransactionEncoder()
    one_hot = encoder.fit(transactions).transform(transactions)
    one_hot_df = pd.DataFrame(one_hot,columns=encoder.columns_)

    apriori_result = apriori(one_hot_df, min_support = min_support, use_colnames = True, verbose = 1)
    df_ar = association_rules(apriori_result, min_threshold = min_confidence)

    df_ar['antecedents'] = df_ar['antecedents'].apply(lambda x: frozenset_to_string(x))
    df_ar['consequents'] = df_ar['consequents'].apply(lambda x: frozenset_to_string(x))
    return df_ar

    
