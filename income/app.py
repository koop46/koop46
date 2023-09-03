"""
income app
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import sqlite3


##########################################################
#SQL
##########################################################

cnx = sqlite3.connect('incomes_DB.db')

MAIN_DF = pd.read_sql_query("SELECT * FROM incomes", cnx).set_index(['index'])



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

    else:
        print("Åldrar måste vara 16-100 och månadssalary 1-100")
