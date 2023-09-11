import pandas as pd
from pyscbwrapper import SCB
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns



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
# Pre-process
##########################################################



df = pd.DataFrame.from_dict(dataset['data'])

ndf1 = pd.DataFrame(df['key'].to_list(), columns = ['Sex', 'Income_class', 'Age', 'Year'])
ndf2 = pd.DataFrame(df['values'].to_list(), columns = ['Average_income', 'Median_income', 'Amount_people'])
df = pd.concat([ndf1, ndf2], axis=1).set_index('Age')


df.drop(['Year'], inplace=True, axis=1)
df.replace('..', 0, inplace=True)
df['Sex'].replace(['1', '2', '1+2'], [1, 0, 2], inplace=True)
df = df.astype({"Amount_people":"int","Average_income":"float", "Median_income":"float"})




JOINT_DF = df.iloc[4420:]
MEN_DF = df.iloc[:2210]
WOMEN_DF = df.iloc[2210:4420]



########################################################################################## Amount


AMOUNT_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(AMOUNT_DF):
    column = JOINT_DF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Amount_people") ] # All

    AMOUNT_DF[col] = column.values

AMOUNT_DF.loc['Summa'] = AMOUNT_DF.sum(axis = 0)
AMOUNT_DF['Totala'] = AMOUNT_DF.sum(axis=1)



MEN_AMOUNT_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(MEN_AMOUNT_DF):
  column = MEN_DF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Amount_people") ] # Men
  MEN_AMOUNT_DF[col] = column.values

MEN_AMOUNT_DF.loc['Summa'] = MEN_AMOUNT_DF.sum(axis = 0)
MEN_AMOUNT_DF['Totala'] = MEN_AMOUNT_DF.sum(axis=1)



WOMEN_AMOUNT_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(WOMEN_AMOUNT_DF):
  column = WOMEN_DF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Amount_people") ] # Women
  WOMEN_AMOUNT_DF[col] = column.values

WOMEN_AMOUNT_DF.loc['Summa'] = WOMEN_AMOUNT_DF.sum(axis = 0)
WOMEN_AMOUNT_DF['Totala'] = WOMEN_AMOUNT_DF.sum(axis=1)


########################################################################################## Average


AVERAGE_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(AVERAGE_DF):
  column = JOINT_DF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Average_income") ] # All
  AVERAGE_DF[col] = column.values



MEN_AVERAGE_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(MEN_AVERAGE_DF):
  column = MEN_DF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Average_income") ] # Men
  MEN_AVERAGE_DF[col] = column.values



WOMEN_AVERAGE_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(WOMEN_AVERAGE_DF):
  column = WOMEN_DF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Average_income") ] # Women
  WOMEN_AVERAGE_DF[col] = column.values


########################################################################################## Median


MEDIAN_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(MEDIAN_DF):
  column = JOINT_DF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Median_income") ] # All
  MEDIAN_DF[col] = column.values



MEN_MEDIAN_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(MEN_MEDIAN_DF):
  column = MEN_DF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Median_income") ] # Men
  MEN_MEDIAN_DF[col] = column.values



WOMEN_MEDIAN_DF = pd.DataFrame( columns = INCOME_CLASSES, index =  AGES )

for idx, col in enumerate(WOMEN_MEDIAN_DF):
  column = WOMEN_DF.iloc[ 85*idx : 85 + 85*idx, df.columns.get_loc("Median_income") ] # Women
  WOMEN_MEDIAN_DF[col] = column.values


##########################################################
# Functions
##########################################################


def income_class(monthly_income):

  yearly_income = monthly_income * 12

  if monthly_income == 0: income_interval = "0"        
  elif monthly_income > 83: income_interval = "1000+ tkr"

  else:
      for col in INCOME_CLASSES[:, 1:-2]: #loop through column names / maybe switch to list with names?
          income_range = col[:-4].split("-")

          if int(income_range[0]) <= yearly_income <= int(income_range[1]):
              income_interval = f"{income_range[0]}-{income_range[1]} tkr"
              break

  class_idx = AMOUNT_DF.columns.get_loc(income_interval) #return income class index
  
  return class_idx


##########################################################
#Streamlit
##########################################################


header = st.container()
body = st.container()

with header:

  st.title("Antal per inkomstklass: Riket")

  XX = WOMEN_AMOUNT_DF.iloc[-1, :-1]
  XY = MEN_AMOUNT_DF.iloc[-1, :-1]
  BARS = pd.concat([XX, XY], axis=1)
  
  fig = plt.figure (figsize=(16, 4) )
  sns.set_style("darkgrid") #Size & style 
  ax = BARS.plot(kind='bar', stacked=True, color=['plum', 'cornflowerblue'])
  ax.set_yticklabels(["0", "200k", "400k", "600k", "800k", '1M', '1.2M'])
  plt.legend([],[], frameon=False)

  plt.gcf().set_facecolor('black') 
  ax.tick_params(axis='x', colors='white')
  ax.tick_params(axis='y', colors='white')


  
  st.pyplot(plt.gcf())


with st.sidebar:
  st.sidebar.subheader('Stats')

  s_form = st.form("stats_form")
  age = s_form.number_input("Ålder", step=1,min_value=16, max_value=100, value=35)
  salary = s_form.number_input("Månadslön i tkr", format= "%.1f",
                                step=.5,min_value=0.0, max_value=100.0, value=35.0)

  if s_form.form_submit_button("Klicka"):
      pass



with body:
  st.header(f"Födda -{2023-age-1900}, bruttosalary: {int(salary*1000):,} kr")


  salary = float(salary)

  if 16 <= age <= 100 and 1 <= salary <= 100:
      pass



      #stats(salary, age)
    #  idx = salarye_index(salary)
      # visualizations(age, salary, idx)




