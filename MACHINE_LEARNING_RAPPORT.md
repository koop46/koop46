# Machine Learning: Linjär regression 

Dom vanligaste stegen i maskininlärningsalgoritmen är sex stycken: 

0) Ändamål
1) Insamling & lagring av data 
2) Utforskning & förbehandling datan 
3) Modelval & träning 
4) Test & utvärdering
5) Driftsättning

### Ändamål
Första steget i ett maskininlärnings- eller deep learningsprojekt är att svara på frågan: Vad har projektet för ändamål? Svaret låter oss bättre välja algoritm och prestationsmått samt tid vi lägger på att justera modellen. Eftersom vi vet att vi vill förutspå huspriser baserat på features så vet vi att vi behöver använda en linjär regressions modell.

Sen är frågan om resultatet av denna modell är den slutgiltiga produkten eller om det ska användas som data i ytterliggar en modell.
I så fall kanske en annan modell lämpar sig bättre.


### Insamling & lagring av data

Data kan samlas in på många olika sätt. Det enklaste är större etablablerade hemsidor som oftast erbjuder färdiga dataset, även om bäst data nog samlas från fastighetsbyråer själva. Fördelen med färdiga dataset är att dom kan innehålla features man inte trodde påverkade priset. Färdiga dataset brukar också komma i format som CSV (comma-separated values), JSON(JavaScript Object Notation) eller XLSX/XLS som är standardformatet för Microsoft Excel.

Beroende på datasetets storlek kan en Excel fil räcka som lagring. För lite större data är nog en SQL databas mer lämplig, och helst i en cloud service.
Efter att datan är införskaffad kan det vara bra att ta en snabb titt på datans dimensioner, det gör vi först genom att öppna datan i en dataframe med hjälp av Pandas biblioteket. Det är också bra att åsido sätta 20% av datan till träningsset, då den korta överblicken kan leda till _data snooping bias_.
Resten av datan blir tränings set för modellen. Data i seten ska också vara slumpmässig. Biblioteket numpy har funktioner för att skriva en funktion som randomiserar datan.


### Utforskning & förbehandling datan
Sen är det dags att utforska datan genom att visualisera den. Dels för att få djupare insikt, dels för att se om du kan upptäcka samband i grafiken. Två bibliotek för att visualisera data är Matplotlib och Seaborn. Beroende på källa kan dataseten innehålla irrelevant data eller föråldrad data som behöver förarbetas. Pandas biblioteket hjälper oss med allt från att inkludera/exkludera värden till att eliminera/ersätta saknade värden samt ändra format på data genom att koda textdata till sifferdata eller ändra datatyp. En sekvens som förbehandlar data kallas för en pipeline. Biblioteket SciKit-Learn har bra moduler för att skapa pipelines.

![Graf](https://github.com/koop46/koop46/blob/main/output1.png?raw=true)

### Model & träning
Nu är det dags att träna linjär regression modellen. Linjär regression är en teknik för prediktiv analys, alltså för att förutspå värden, och klassas som supervised learning. Det innebär att modellen tränas på datapunkter (exempelvis kvadratstorlek) med respektive labels (huspris). Modellen beräknar sambandet mellan punkter och labels för att producerar en linjär ekvation med en linje, en lutning som beskriver sambandet. I detta fall hur mycket huspriset ökar ju mer storleke på huset ökar. Det är detta linjära samband som kallas linjär regression och träningen av modellen sker med hjälp av SciKit-Learn.


$y = Wx + b$

![Graf](https://github.com/koop46/koop46/blob/main/output.png?raw=true)

Träningen sker på dom 80% vi åsidosatte i början och kan ta en stund att genomföra beroende på storlek och processkapacitet. Det är under träningsfasen algoritmen också använder sig av kostnadsfuntionen. Den vi har valt är Root Mean Square Error (RMSE). RMSE mäter felmarginalen genom att kvadrera differensen mellan det prediktiva värdet och det faktiska värdet i vartenda träningsexempel; delar summan av alla träningsexempel på antalet exempel och beräknar roten ur denna kvot. Modellen finjusteras sedan för att minska kostnadsfunktionens resultat så mycket som möjligt.


RMSE(X,h) = $\sqrt{\frac{1}{m} \Sigma_{i=1}^{m} (h(x^i) - y^i)^2}$

### Test & utvärdering 

Till sist testar vi modellen på dom återstående 20% av datan. Här finns även risken att fortsätta justera modellen för att prediktionerna ska komma så nära dom faktiskt huspriserna som möjligt. Men då ökar risken för att modellen anpassar sig så mycket efter träningsdatan att den presterar dåligt på ny data. Så kallad overfitting.


### Driftsättning 

Slutligen vill vi driftsätta modellen. För det finns det olika plattformar som till exempel Amazon Web Service (AWS) eller Google Cloud AI. Det går även att driftsätta den från en egen server. För lite enklare ML modeller kan Streamlit plattformen fungera ganska bra. 
På Streamlit kan man bygga en enkel frontend med deras Streamlit bibliotek, ladda upp sitt script och lansera sin modell.



[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/8M20LyCZDOY/0.jpg)](https://www.youtube.com/watch?v=8M20LyCZDOY)



## Källor

zenrows.com/blog/collecting-data-to-map-housing-prices#the-map 
scaler.com/topics/pandas/datasets-in-pandas/ 
towardsdatascience.com/what-i-learned-setting-up-storage-for-a-machine-learning-project-7ae1e5668762 
towardsdatascience.com/the-complete-guide-to-linear-regression-analysis-38a421a89dc2 
medium.com/analytics-vidhya/linear-regression-in-7-steps-b7362af795aa 
analyticsvidhya.com/blog/2021/10/everything-you-need-to-know-about-linear-regression/#:~:text=Linear%20regression%20is%20a%20quiet,%2Daxis%2C%20called%20linear%20regression.
w3schools.com/python/pandas/pandas_cleaning_wrong_format.asp
projectpro.io/article/machine-learning-model-deployment/872#:~:text=You%20can%20deploy%20machine%20learning,time%20inference%20at%20the%20edge.
stackoverflow.blog/2020/10/12/how-to-put-machine-learning-models-into-production/
projectpro.io/article/machine-learning-model-deployment/872#:~:text=You%20can%20deploy%20machine%20learning,time%20inference%20at%20the%20edge.

