#  Groene leefomgeving

Mensen die in een groene omgeving wonen, voelen zich niet alleen gezonder, ze zijn het ook. Onderzoek wijst uit dat bewoners van een groene omgeving minder vaak een huisarts bezoeken met klachten als diabetes,hart-en vaatziekten en depressie. Ook zorgt groen in de buurt voor minder stress (gezonde leefomgeving. 13 april, 2022). 

In deze repo onderzoeken we verschillende openbare Databronnen om aan de hand van verschillende methoden de groene leefomgeving te bepalen. 



**Files uitleg:** 

    - Groene-Leefomgeving.ipynb : De jupyter notebook waar we uitleg geven over onze databronnen ,methoden en eventueel downloaden van Satelliet  images. 


    - data : Deze file bevat .CSV data die worden gemaakt door Qgis model (Vegation op gemeenten / buurt niveau). 

    - Qgis_project : Deze file bevat (Tct_model) en (ndvi_model) om vegation op buurt en gemeenten nieavu te berekenen. De modellen zijn ook als .py bestanden te vinden. Er zijn ook buurten.gpkg en gemeenten.gpkg deze zijn buurt en gemeenten grenzen uit PDOK. Verder zijn er Satelliet beelden uit Groene-Leefomgeving.ipynb. 


**Benodige liberies :** 

    - Pandas 
    -numpy 
    - ee (Google earth engine) 
    -folium 
    -geehydro 
    -matplotlib
    -seaborn  


**Google eath engine :**

- API aanvragen : https://signup.earthengine.google.com/ 

- python Installation : 
    

------------------------------
Conda Package Manager:
------------------------------
conda update -c conda-forge earthengine-api
------------------------------

---------------------------
Python Package Installer: 
-------------------------
pip install earthengine-api --upgrade
------------------------- 

- Meer info :
    https://developers.google.com/earth-engine/guides/python_install 


**Qgis :**

- Download Qgis software : 
    https://qgis.org/en/site/forusers/download.html 

- Download PDOK plugin :
    1. Start qgis software 
    2. in het bovenste panel ga naar "Plug-ins"
    3. vervolgens "Manage and Install Plugins".
    4. klik op het tabblad Alles en zoek naar "PDOK services plugin.
    5. pulg-in installeren.+ 
    
