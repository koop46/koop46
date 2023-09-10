import pandas as pd
from pyscbwrapper import SCB


##########################################################
# API call
##########################################################


AGES = [f'{y} år' if y < 100 else '100+ år' for y in range(16,101)]
INCOME_CLASSES = ['0', '1-19 tkr', '20-39 tkr', '40-59 tkr', '60-79 tkr', '80-99 tkr', 
                            '100-119 tkr', '120-139 tkr', '140-159 tkr', '160-179 tkr', '180-199 tkr', 
                            '200-219 tkr', '220-239 tkr', '240-259 tkr', '260-279 tkr', '280-299 tkr', 
                            '300-319 tkr', '320-339 tkr', '340-359 tkr', '360-379 tkr', '380-399 tkr', 
                            '400-499 tkr', '500-599 tkr', '600-799 tkr', '800-999 tkr', '1000+ tkr']

scb = SCB('sv', 'HE', 'HE0110', 'HE0110A', 'SamForvInk1a')
scb.set_query(kön = ["män", "kvinnor", "totalt"],
               tabellinnehåll = ["Medelinkomst, tkr", "Medianinkomst, tkr", "Antal personer"], 
               år = ['2021'], AGESer = AGES, inkomstklass = INCOME_CLASSES)

scb.get_query()
dataset = scb.get_data()


##########################################################
# Data cleaning
##########################################################


df = pd.DataFrame.from_dict(dataset['data'])

ndf1 = pd.DataFrame(df['key'].to_list(), columns = ['Sex', 'Income_class', 'Age', 'Year'])
ndf2 = pd.DataFrame(df['values'].to_list(), columns = ['Average_income', 'Median_income', 'Amount_people'])
df = pd.concat([ndf1, ndf2], axis=1).set_index('Age')


df.drop(['Year'], inplace=True, axis=1)
df.replace('..', 0, inplace=True)
df['Sex'].replace(['1', '2', '1+2'], [1, 0, 2], inplace=True)
df = df.astype({"Amount_people":"int","Average_income":"float", "Median_income":"float"})




JDF = df.iloc[4420:]
MDF = df.iloc[:2210]
WDF = df.iloc[2210:4420]



###### Amount

MAIN_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(MAIN_DF):
    column = JDF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Amount_people") ] # All

    MAIN_DF[col] = column.values

MAIN_DF.loc['Summa'] = MAIN_DF.sum(axis = 0)
MAIN_DF['Totala'] = MAIN_DF.sum(axis=1)



MEN_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(MEN_DF):
  column = MDF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Amount_people") ] # Men
  MEN_DF[col] = column.values

MEN_DF.loc['Summa'] = MEN_DF.sum(axis = 0)
MEN_DF['Totala'] = MEN_DF.sum(axis=1)



WOMEN_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(WOMEN_DF):
  column = WDF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Amount_people") ] # Women
  WOMEN_DF[col] = column.values

WOMEN_DF.loc['Summa'] = WOMEN_DF.sum(axis = 0)
WOMEN_DF['Totala'] = WOMEN_DF.sum(axis=1)


###### Average

AVERAGE_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(AVERAGE_DF):
  column = JDF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Average_income") ] # All
  AVERAGE_DF[col] = column.values



MEN_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(MEN_DF):
  column = MDF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Average_income") ] # Men
  MEN_DF[col] = column.values



WOMEN_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(WOMEN_DF):
  column = WDF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Average_income") ] # Women
  WOMEN_DF[col] = column.values


###### Median

MEDIAN_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(MEDIAN_DF):
  column = JDF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Median_income") ] # All
  MEDIAN_DF[col] = column.values



MEN_MEDIAN_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(MEN_MEDIAN_DF):
  column = MDF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Median_income") ] # Men
  MEN_MEDIAN_DF[col] = column.values



WOMEN_MEDIAN_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(WOMEN_MEDIAN_DF):
  column = WDF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Median_income") ] # Women
  WOMEN_MEDIAN_DF[col] = column.values








