"""
income app
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_gsheets import GSheetsConnection


##########################################################
#SQL
##########################################################

cnx = st.experimental_connection('incomes_db', type='sql')

#income tables
incomes = cnx.query("SELECT * FROM incomes").set_index(['index'])
MAIN_DF = st.dataframe(incomes)

#pd.read_sql_query("SELECT * FROM incomes", cnx).set_index(['index'])

#MEN_DF_ = pd.read_sql_query("SELECT * FROM incomes_m", cnx).set_index(['index'])

#WOMEN_DF = pd.read_sql_query("SELECT * FROM incomes_w", cnx).set_index(['index'])

#median tables
#MEDIAN_DF = pd.read_sql_query("SELECT * FROM medians", cnx).set_index(['index'])

#MEDIAN_DF_M = pd.read_sql_query("SELECT * FROM median_m", cnx).set_index(['index'])

#MEDIAN_DF_W = pd.read_sql_query("SELECT * FROM median_w", cnx).set_index(['index'])


##########################################################
#Functions
##########################################################

def income_class(monthly_income):

    yearly_income = monthly_income * 12

    if monthly_income == 0: income_interval = "0"        
    elif monthly_income > 83: income_interval = "1000+ tkr"

    else:
        for col in MAIN_DF.iloc[:, 1:-2]: #loop through column names / maybe switch to list with names?
            income_range = col[:-4].split("-")

            if int(income_range[0]) <= yearly_income <= int(income_range[1]):
                income_interval = f"{income_range[0]}-{income_range[1]} tkr"
                break

    class_idx = MAIN_DF.columns.get_loc(income_interval) #return income class index
    return class_idx





##########################################################
#Streamlit
##########################################################


header = st.container()
body = st.container()

with header:

    st.title("Storlek på inkomstklass: Riket")

    #Välkomnst graf
    colors_1 = ["darkgreen" for i in range(26)]
    fig, ax1 = plt.subplots()
    fig.patch.set_facecolor('whitesmoke')
    ax1.set_facecolor('whitesmoke')
    ax1.set_yticklabels(('0', '200k', '400k', '600k', '800k', "1 mil.", "1.2 mil"))


    MAIN_DF.iloc[85,:26].T.plot.bar(ax=ax1, color=colors_1, figsize=(18,6))
    plt.show()
    st.pyplot(fig)


    #tabell
#    alla_df.T[["Summa"]].T



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

