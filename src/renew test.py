import pandas as pd
import numpy as np

renew = pd.read_csv(r'/Users/henryhundt/PycharmProjects/Racine_WI/Data/pv.commercial.systems.renew.maptive.csv')
cond_ = (renew["City"] == 'Madison') & (renew["Year Installed"] == "2016")
renew.loc[cond_]
madison_2016 = renew.loc[cond_]

#first method, go one criteria at a time)
#renew.dtypes
#print(renew['City'])
#print(renew[renew.City == 'Madison'])

#how to take last print and make into data frame that I can export to csv.
madison = renew[renew.City == 'Madison']