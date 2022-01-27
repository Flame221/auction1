import pandas as pd

data = {
    'Name': ['Visa', 'Mastercard', 'American Express', 'Diners Club'],
    'Number': ['0001', '0002', '0003', '0004'],
    'Balance': [100, 10000, 3000, 1000]
}

cards_data1 = pd.DataFrame(data)
cards_data1.index = cards_data1.index + 1