import pandas as pd

census = pd.read_csv(r"/Users/henryhundt/Desktop/Graduate School/HP Python Independent Study/df_census.csv")
print(census)

census = census[(census["State"] == "WI") & (census["Heatpumps?"] == 1.0)]
print(census)
#only 69 rows with heatpumps in WI. What does that mean in this context?