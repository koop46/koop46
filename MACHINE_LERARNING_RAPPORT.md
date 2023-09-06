# Machine Learning: Linjär regression 

Dom vanligaste stegen i maskininlärningsalgoritmen linjär regression är sex stycken: 

1) Insamling & lagring av data 
2) Visualisering & utforskning (EDA) 
3) Bearbetning av data
4) Model & träning 
5) Test & utvärdering  
6) Driftsättning

 

### Insamling & lagring av data 

Data kan samlas in på många olika sätt, men det enklaste är nog att ta ladda ner färdiga dataset från större fastihetshemsidor. Beroende på källa kan dataseten innehålla irrelevant data, som behöver elimineras under bearbetingen, eller föråldrad data. Bästa data går nog att samla från fastighetsägarna själva. Om du väljer att samla in själv så avgör du formatet för datan, annars brukar datan sammanställas i tabeller med format som CSV (comma-separated values), JSON(JavaScript Object Notation) eller XLSX/XLS som är standardformatet för Microsoft Excel.  
Beroende på datasetets storlek kan det räcka med en SQL databas på hårddisken, USB sticka eller molnet för lagring. För lite större dataset hade nog en egen databas fungerat bättre. 

Efter datan är säkrad vill man nog visualisera den. Enklast går det att göra med hjälp av Python biblioteken Matplotlib (as plt) eller det senare Seaborn (as sns). Det kan se ut såhär: 

[Insert graph] 

 

 

### Visualisering & utforskning (EDA) 

### Bearbetning av data 

Kolla missing values,  

### Model & träning 

Linjär regression är en teknik för att prediktiv analys, alltså för att förutspå värden. Det funkar som så att värden matas in i en linjär regressionsalgoritm, i detta fall huspriser och, för enkelhetens skull, kvadratstorlek på hus. Algoritmen genererar en graf med x världen (kvadratstorlek) och y värden (huspris) och en linje, precis som en linjär ekvation. På grafen går det då att se sambandet att ju större storlek på huset desto högre är priset. Lutningen(w) på linjen representerar hur mycket priset ökar per 10 kvadratmeter, och skärningen i y-axeln (b) var priset börjar. 

[insert graph] 

Tänk nu att en sån här linjär regressionsmodell tränas med tusentals huspriser och respektive egenskaper eller features som det kallas. Storlek på rum, geografisk position, ålder på fastighet etcetera. Vi får då en modell med väldigt hög precision i att förutspå pris på ett hus med givna egenskaper. Ungefär som en väldigt erfaren mäklare.  

### Test & utvärdering 

 

Men det kan också uppstå fel i prediktionen, hus kan varderas för högt eller för lågt beroende på dess parametrarna (w) och (b), alltså begynnelsepris och ökningen i pris. Ett sätt att minska felmarginalen är med hjälp av en kostnadsfunktion. Kostnadsfunktionen mäter felmarginalen genom att kvadrera differensen mellan det prediktiva värdet och det faktiska värdet i vartenda träningsexempel; summera allt och delar denna summa på antalet träningsset gånger 2. 
Detta kallas squared error cost function: 

J(w,b) = $\frac{1}{2m} \Sigma_{i=1}^{m} (\hat{y}^i - y^i)^2$

 

### Driftsättning 

För att driftsätta modellen finns det en väldigt användbar plattform vid namn Streamlit. 
På Streamlit kan man ladda upp sitt script, bygga en enkel frontend och lansera en enkel webapp. 




 <video width="320" height="240" controls>
  <source src="https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4
" type="mp4">
</video>

zenrows.com/blog/collecting-data-to-map-housing-prices#the-map 

scaler.com/topics/pandas/datasets-in-pandas/ 

towardsdatascience.com/what-i-learned-setting-up-storage-for-a-machine-learning-project-7ae1e5668762 

towardsdatascience.com/the-complete-guide-to-linear-regression-analysis-38a421a89dc2 

medium.com/analytics-vidhya/linear-regression-in-7-steps-b7362af795aa 

 

 