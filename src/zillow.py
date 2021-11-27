import pandas as pd


zillow = pd.read_csv(r"/Users/henryhundt/Desktop/Graduate School/HP Python Independent Study/df_zillow.csv", nrows=1000)
print(zillow)
zillow.dtypes
zillow['HeatingType'].value_counts()




#for chunk in pd.read_csv(r"/Users/henryhundt/Desktop/Graduate School/HP Python Independent Study/df_zillow.csv"):





#
#for iter_num, chunk in enumerate(zillow, 1):
    #print(f'Processing iteration {iter_num}')