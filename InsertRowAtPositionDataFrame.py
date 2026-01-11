# Write a program to insert row at a given position in pandas DataFrame.

import pandas as pd

data = {
    'Name': ['Amana', 'Amalu', 'Amina'],
    'Age': [20, 21, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

new_row = {'Name': 'Anagha', 'Age': 21, 'City': 'Miami'}

position = 1

df = pd.concat([df[:position], pd.DataFrame([new_row]), df[position:]]).reset_index(drop=True)

print(df)

# OUTPUT:
#     Name   Age        City
# 0  Amana   20     New York
# 1  Anagha  21        Miami
# 2  Amalu   21   Los Angeles
# 3  Amina   22      Chicago
