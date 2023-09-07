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
Här kan det vara bra att ta en snabb titt på datans dimensioner, det gör vi först genom att öppna datan i en dataframe med hjälp av Pandas biblioteket. `df = pandas.read_sql('huspriser.db')` om datan är i SQL format eller `df = pandas.read_excel('huspriser.xlsx')` det är excel format. Det är också bra att skapa ett test set här då den korta överblicken kan leda till _data snooping bias_.
Test set brukar utgöra 20% av totala datan, resten av datan blir tränings set för modellen. Data i seten ska också vara slumpmässig, biblioteket numpy har funktioner för att skriva en funktion som randomiserar set.

***ändra format

### Utforskning & förbehandling datan
Sen är det dags att utforska datan genom att visualisera. Dels för att få djupare insikt, dels för att se om du kan upptäcka samband i grafiken. Två bibliotek för att visualisera data är Matplotlib och Seaborn. Bibliteket Pandas har bra verktyg för den uppgiften. Beroende på källa kan dataseten innehålla irrelevant data eller föråldrad data som behöver bearbetas. Pandasbiblioteket hjälper oss med allt från att inkludera eller exkludera vissa värden eller features modellen kommer utgå ifrån. Till att ersätta eller eliminera saknade värden och att koda textdata till sifferdata. En sekvens steg som förbehandlar data kallas för en pipeline. Biblioteket SciKit-Learn har bra moduler för att skapa pipelines.

![Graf](https://github.com/koop46/koop46/blob/main/output1.png?raw=true)

### Model & träning 
Linjär regression är en maskininlärningsmodell för prediktiv analys, för att förutspå värden. Den klassas som supervised learning då modellen tränas på datapunkter (input) med respektive labels (output). Modellen beräknar sambandet mellan punkterna och producerar en linje, lutning, som bäst beskriver samabndet. Resultatet kan visualiseras som en grafen med beroende variabeln i x-led (storlek) och oberoende i y-led(förutspått huspris). Det är detta linjära samband som kallas linjär regression och träningen av modellen sker med hjälp av SciKit-Learn.


$y = Wx + b$

![Graf](https://github.com/koop46/koop46/blob/main/output.png?raw=true)


### Test & utvärdering 

 

Men det kan också uppstå fel i prediktionen, hus kan värderas för högt eller för lågt beroende på dess parametrarna (w) och (b), alltså ökningen i pris och begynnelsepris. Ett sätt att minska felmarginalen är med hjälp av en kostnadsfunktion. Kostnadsfunktionen mäter felmarginalen genom att kvadrera differensen mellan det prediktiva värdet och det faktiska värdet i vartenda träningsexempel; summera allt och delar denna summa på antalet träningsset gånger 2. 
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

analyticsvidhya.com/blog/2021/10/everything-you-need-to-know-about-linear-regression/#:~:text=Linear%20regression%20is%20a%20quiet,%2Daxis%2C%20called%20linear%20regression.


 