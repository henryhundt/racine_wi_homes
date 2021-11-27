# This script opens and pulls all data related to Racine, WI from MEdward's cleaned Zillow data.

import pandas as pd
import numpy as np


#read in zillow data sort for City: Racine, State: WI
zillow = pd.read_csv('Data/df_zillow.csv')
cond_ = (zillow["City"] == 'RACINE') & (zillow["State"] == 'WI')
zillow.loc[cond_]

#new df for Racine WI
racine_wi = zillow.loc[cond_]

#export to CSV file
racine_wi.to_csv('Data/racine_wi.csv', index=False)

