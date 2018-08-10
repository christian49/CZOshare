import pandas as pd
import re
import csv

df_vars = pd.read_csv("open-refine-vars.csv") # ,index_col=0
#var = df_vars['variable']
#czo_id = df_vars['czo_id']
#keys = []
print(df_vars.head())
df_discp = pd.read_csv("dataset-discplines.csv") # ,index_col=0
#disciplines = df_vars['DISCIPLINES']
#czo_id = df_vars['czo_id']
print(df_discp.head())

discp_and_vars = df_vars.merge(df_discp,on='czo_id')
print(discp_and_vars.head())

discp_and_vars.to_csv("open-refine-vars-disciplines.csv")