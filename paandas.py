import pandas as pd
pd.set_option('max_rows', 5)
fruits = pd.DataFrame([[30, 21],[35, 40]], columns=['Apples', 'Bananas'], index=["2017", "2018"])
print(fruits)