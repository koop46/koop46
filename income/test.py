import pandas as pd
from pyscbwrapper import SCB


##########################################################
# API call
##########################################################


åld = [f'{y} år' if y < 100 else '100+ år' for y in range(16,101)]
ink = ['0', '1-19 tkr', '20-39 tkr', '40-59 tkr', '60-79 tkr', '80-99 tkr', 
                            '100-119 tkr', '120-139 tkr', '140-159 tkr', '160-179 tkr', '180-199 tkr', 
                            '200-219 tkr', '220-239 tkr', '240-259 tkr', '260-279 tkr', '280-299 tkr', 
                            '300-319 tkr', '320-339 tkr', '340-359 tkr', '360-379 tkr', '380-399 tkr', 
                            '400-499 tkr', '500-599 tkr', '600-799 tkr', '800-999 tkr', '1000+ tkr']

scb = SCB('sv', 'HE', 'HE0110', 'HE0110A', 'SamForvInk1a')
scb.set_query(kön = ["män", "kvinnor", "totalt"],
               tabellinnehåll = ["Medelinkomst, tkr", "Medianinkomst, tkr", "Antal personer"], 
               år = ['2021'], ålder = åld, inkomstklass = ink)

scb.get_query()
dataset = scb.get_data()


##########################################################
# Prepocessing
##########################################################


df = pd.DataFrame.from_dict(dataset['data'])

ndf1 = pd.DataFrame(df['key'].to_list(), columns = ['Sex', 'Income_class', 'Age', 'Year'])
ndf2 = pd.DataFrame(df['values'].to_list(), columns = ['Average_income', 'Median_income', 'Amount_people'])
df = pd.concat([ndf1, ndf2], axis=1).set_index('Age')


df.drop(['Year'], inplace=True, axis=1)
df.replace('..', 0, inplace=True)
df['Sex'].replace(['1', '2', '1+2'], [1, 0, 2], inplace=True)
df = df.astype({"Amount_people":"int","Average_income":"float", "Median_income":"float"})


""" MEN_AVERAGE_DF = pd.DataFrame( columns = ink, index =  åld )
WOMEN_AVERAGE_DF = pd.DataFrame( columns = ink, index =  åld )
AVERAGE_DF = pd.DataFrame( columns = ink, index =  åld )

MEN_MEDIAN_DF = pd.DataFrame( columns = ink, index =  åld )
WOMEN_MEDIAN_DF = pd.DataFrame( columns = ink, index =  åld )
MEDIAN__DF = pd.DataFrame( columns = ink, index =  åld )
 """

jdf = df.iloc[4420:]
mdf = df.iloc[:2210]
wdf = df.iloc[2210:4420]

### Antal
MAIN_DF = pd.DataFrame( columns = ink, index =  åld )

for i, c in enumerate(MAIN_DF):
    col = jdf.iloc[ 85*i : 85 + 85*i, 4 ]
    MAIN_DF[c] = col.values

MAIN_DF.loc['Summa'] = MAIN_DF.sum(axis = 0)
MAIN_DF['Totala'] = MAIN_DF.sum(axis=1)


### Antal män
MEN_DF = pd.DataFrame( columns = ink, index =  åld )

for i, c in enumerate(MEN_DF):
  col = mdf.iloc[ 85*i : 85 + 85*i, 4 ]
  MEN_DF[c] = col.values

MEN_DF.loc['Summa'] = MEN_DF.sum(axis = 0)
MEN_DF['Totala'] = MEN_DF.sum(axis=1)


### Antal kvinnor
WOMEN_DF = pd.DataFrame( columns = ink, index =  åld )

for i, c in enumerate(WOMEN_DF):
  col = wdf.iloc[ 85*i : 85 + 85*i, 4 ]
  WOMEN_DF[c] = col.values

WOMEN_DF.loc['Summa'] = WOMEN_DF.sum(axis = 0)
WOMEN_DF['Totala'] = WOMEN_DF.sum(axis=1)



mdf