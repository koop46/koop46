"""
income app
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


df = pd.read_excel("/workspaces/koop46/income/21d.xlsx")

ages = df.iloc[3:88,1]
income_classes = [ df.iloc[88+85*n, 0] for n in range(26) ]

MAIN_DF = WOMEN_DF = MEN_DF = MEDIAN_DF = MEDIAN_DF_W = MEDIAN_DF_M = pd.DataFrame( columns = income_classes, index = ages )
MAIN_DF.index.name = WOMEN_DF.index.name = MEN_DF.index.name = None
MEDIAN_DF.index.name = MEDIAN_DF_W.index.name = MEDIAN_DF_M.index.name = None


# #######################################################################
# ##############################  Main DF  ##############################
# #######################################################################

for (i,data) in enumerate(MAIN_DF):

    col = df.iloc[ 88 + 85 * i:173 + 85 * i, 8 ]
    MAIN_DF[data] = col.values

MAIN_DF = MAIN_DF.replace("..", 0)
MAIN_DF.loc['Summa'] = MAIN_DF.sum(axis = 0)
MAIN_DF['Totala'] = MAIN_DF.sum(axis=1)


# #######################################################################
# #######################  Men & Women income DF  #######################
# #######################################################################

for (i,data) in enumerate(MEN_DF):

    col = df.iloc[ 88 + 85 * i:173 + 85 * i, 4 ]
    MEN_DF[data] = col.values

MEN_DF = MEN_DF.replace("..", 0)
MEN_DF.loc['Summa'] = MEN_DF.sum(axis = 0)
MEN_DF['Totala'] = MEN_DF.sum(axis=1)



for (i,data) in enumerate(WOMEN_DF):

    col = df.iloc[ 88 + 85 * i:173 + 85 * i, 6 ]
    WOMEN_DF[data] = col.values

WOMEN_DF = WOMEN_DF.replace("..", 0)
WOMEN_DF.loc['Summa'] = WOMEN_DF.sum(axis = 0)
WOMEN_DF['Totala'] = WOMEN_DF.sum(axis=1)


# #######################################################################
# ########################  Median DF M, W & All ########################
# #######################################################################

for (i,data) in enumerate(MEDIAN_DF):

    col = df.iloc[ 88 + 85 * i:173 + 85 * i, 7 ]
    MEDIAN_DF[data] = col.values

MEDIAN_DF = MEDIAN_DF.replace("..", 0)



for (i,data) in enumerate(MEDIAN_DF_M):

    col = df.iloc[ 88 + 85 * i:173 + 85 * i, 3 ]
    MEDIAN_DF_M[data] = col.values

MEDIAN_DF_M = MEDIAN_DF_M.replace("..", 0)



for (i,data) in enumerate(MEDIAN_DF_W):

    col = df.iloc[ 88 + 85 * i:173 + 85 * i, 5 ]
    MEDIAN_DF_W[data] = col.values

MEDIAN_DF_W = MEDIAN_DF_W.replace("..", 0)



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
