import numpy as np
import pandas as pd

data = {
    'Item': ['iPhone 12 Pro', 'Konsola Playstation 5', 'Bluza Adidas Męska Szara', 'Spodnie Wrangler Arizona',
             'Basen ogrodowy Premium', 'Krzesło skandynwskie granatowe'],
    'Category': ['elektronika', 'elektronika', 'odzież', 'odzież', 'dom i ogród', 'dom i ogród'],
    'Price': [4600, 2899, 249, 189, 1199, 88],
    'Selection': [True, False, True, False, False, False]
}
goods_data1 = pd.DataFrame(data)
goods_data1 = goods_data1.sort_values(by='Selection', ascending=False)
goods_data1 = goods_data1.reset_index(drop=True)
goods_data1.index = goods_data1.index + 1
