# This script opens and pulls all census data related to Racine, WI from Morgan Edward's cleaned and combined census df

import pandas as pd
import numpy as np

#read in cansus data
#census_csv = 'df_census.csv'

zillow = pd.read_csv('Data/df_zillow.csv')
cond_ = (zillow["City"] == 'RACINE') & (zillow["State"] == 'WI')
zillow.loc[cond_]
racine_wi = zillow.loc[cond_]

racine_wi.to_csv('Data/racine_wi.csv', index=False)

#learning process
#zillow_smalltest = zillow.head(1000)
#zillow_smalltest.dtypes
#print(zillow_smalltest[zillow_smalltest.City == 'MARBURY'])
#marbury = zillow_smalltest[zillow_smalltest.City == 'MARBURY']
#marbury_gv = marbury[marbury.HeatingType == 'GV']

#arbury_gv.to_csv('data/df_marbury_gv.csv', index=False)