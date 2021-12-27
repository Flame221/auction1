import pandas as pd
import numpy as np
from colorama import init, Fore

data = {
    'Item': ['iPhone 12 Pro', 'Konsola Playstation 5', 'Bluza Adidas Męska Szara', 'Spodnie Wrangler Arizona',
             'Basen ogrodowy Premium', 'Krzesło skandynwskie granatowe'],
    'Category': ['elektronika', 'elektronika', 'odzież', 'odzież', 'dom i ogród', 'dom i ogród'],
    'Price': [4600, 2899, 249, 189, 1199, 88],
    'Selection': [True, False, True, False, False, False]
}
goods_data1 = pd.DataFrame(data)
df = goods_data1.sort_values(by='Selection', ascending=False)
df = df.reset_index(drop=True)
df.index = df.index + 1
df1 = df.loc[df['Selection'] == True] + Fore.YELLOW
print(df1)


print(goods_data1)
print('\n' * 5)
print(df)
