import pprint
import pandas as pd
from datetime import date


def stats_generate(txtfile):
    today = date.today()
    today = int(str(today).split("-")[-1])
    
    
    df = pd.read_csv(txtfile)
    print('Brief Summary')
    print(df.groupby(['category', 'category_explain']).sum()['amount'])
    
    print("\n")
    
    print('Last 7 Days Expenses')
    dx = df[df['date'] >= today -7]
    dff = dx.groupby(['category', 'category_explain']).sum()['amount']
    print(dff)
        
