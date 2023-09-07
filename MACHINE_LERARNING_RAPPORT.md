# Machine Learning: Linjär regression 

Dom vanligaste stegen i maskininlärningsalgoritmen är sex stycken: 

0) Syfte
1) Insamling & lagring av data 
2) Utforskning & förbehandling datan 
3) Modelval & träning 
4) Test & utvärdering
5) Driftsättning

### Ändamål
Första steget i ett maskininlärnings- eller deep learningsprojekt är att svara på frågan: Vad har projektet för ändamål? Svaret låter oss bättre välja algoritm och prestationsmått samt tid vi lägger på att justera modellen. Eftersom vi vet att vi vill förutspå huspriser baserat på features så vet vi att vi behöver använda en linjär regressions modell.
För att mäta prestation är ett sedvanligt prestationsmått Root Mean Square Error(RMSE):

RMSE(X,h) = $\sqrt{\frac{1}{m} \Sigma_{i=1}^{m} (h(x^i) - y^i)^2}$

En formel som mäter hur långt ifrån faktiska priset som modellens prediktioner kommer hamna.
Sen är frågan om resultatet av denna modell är den slutgiltiga produkten eller om det ska användas som data i ytterliggar en modell.
I så fall kanske en annan modell lämpar sig bättre.


### Insamling & lagring av data

Data kan samlas in på många olika sätt, det enklaste är större etablablerade hemsidor som oftast erbjuder färdiga dataset. Bäst data samlas nog från fastighetsbyråer själva. Fördelen med färdiga dataset är att dom kan innehålla features man inte trodde påverkade priset. Färdiga dataset brukar också komma i format som CSV (comma-separated values), JSON(JavaScript Object Notation) eller XLSX/XLS som är standardformatet för Microsoft Excel. Beroende på datasetets storlek kan det räcka med en Excel fil, speciellt då Python kod numera går att köra direkt i filen. För lite större data är nog en SQL databas mer lämplig. Och helst att lagra den på molnet.
Här kan det vara bra att ta en snabb titt på datans dimensioner, det gör vi först genom att öppna datan i en dataframe med hjälp av Pandas biblioteket. `df = pandas.read_sql('huspriser.db')` om datan är i SQL format eller 'df = pandas.read_excel()` det är excel format. Sen kan vi tillämpa metoderna:
`df.head()`, `df.describe()`, `df.head()` och `df.info()`

### Utforskning & förbehandling datan
Men Beroende på källa kan dataseten innehålla irrelevant data, som behöver elimineras under bearbetingen, eller föråldrad data. 
Efter datan är säkrad vill man nog visualisera den. Enklast går det att göra med hjälp av Python biblioteken Matplotlib (as plt) eller det senare Seaborn (as sns). Det kan se ut såhär: 

[Insert graph] 


Kolla missing values,  

### Model & träning 

Linjär regression är en teknik för att prediktiv analys, alltså för att förutspå värden. Det funkar som så att värden matas in i en linjär regressionsalgoritm, i detta fall huspriser och, för enkelhetens skull, kvadratstorlek på hus. Algoritmen genererar en graf med x världen (kvadratstorlek) och y värden (huspris) och en linje, precis som en linjär ekvation. På grafen går det då att se sambandet att ju större storlek på huset desto högre är priset. Lutningen(w) på linjen representerar hur mycket priset ökar per 10 kvadratmeter, och skärningen i y-axeln (b) var priset börjar. 

[insert graph] 

Tänk nu att en sån här linjär regressionsmodell tränas med tusentals huspriser och respektive egenskaper eller features som det kallas. Storlek på rum, geografisk position, ålder på fastighet etcetera. Vi får då en modell med väldigt hög precision i att förutspå pris på ett hus med givna egenskaper. Ungefär som en väldigt erfaren mäklare.  

### Test & utvärdering 

 

Men det kan också uppstå fel i prediktionen, hus kan varderas för högt eller för lågt beroende på dess parametrarna (w) och (b), alltså begynnelsepris och ökningen i pris. Ett sätt att minska felmarginalen är med hjälp av en kostnadsfunktion. Kostnadsfunktionen mäter felmarginalen genom att kvadrera differensen mellan det prediktiva värdet och det faktiska värdet i vartenda träningsexempel; summera allt och delar denna summa på antalet träningsset gånger 2. 
Detta kallas squared error cost function: 


 

### Driftsättning 

För att driftsätta modellen finns det en väldigt användbar plattform vid namn Streamlit. 
På Streamlit kan man ladda upp sitt script, bygga en enkel frontend och lansera en enkel webapp. 



[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/8M20LyCZDOY/0.jpg)](https://www.youtube.com/watch?v=8M20LyCZDOY)




zenrows.com/blog/collecting-data-to-map-housing-prices#the-map 

scaler.com/topics/pandas/datasets-in-pandas/ 

towardsdatascience.com/what-i-learned-setting-up-storage-for-a-machine-learning-project-7ae1e5668762 

towardsdatascience.com/the-complete-guide-to-linear-regression-analysis-38a421a89dc2 

medium.com/analytics-vidhya/linear-regression-in-7-steps-b7362af795aa 

 

 