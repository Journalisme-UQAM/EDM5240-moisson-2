### MES COMMENTAIRES ET CORRECTIONS SONT MARQUÉS PAR TROIS DIÈSES

### Exercice intéressant
### Ton script fonctionne et il est bien commenté
### Cependant, il ne produit pas le CSV attendu
### En outre, un site comme celui-là (tout comme les sites de données ouvertes) ne nécessitent pas de moissonnage
### Un bouton «Download» permet de télécharger une version tableur des données affichées

#coding: utf-8

#On importe les modules dont on va avoir besoin, dont BeautifulSoup
import csv
import requests
from bs4 import BeautifulSoup

#Les données qu'on veut aujourd'hui, ce sont des données ouvertes de l'ONU qui donnent la production d'éléectricité du Canada en fonction de l'année (de 1990 à 2014)
url="http://data.un.org/Data.aspx?q=canada&d=EDATA&f=cmID%3aEH%3bcrID%3a124"

#Comme on va fouiller dans un site internet, on laisse entetes comme signature, pour que le site sache qui c'est qui vient chercher des choses chez eux.
entetes={
    "User-Agent":"Bonjour ! Je m'appelle Shannon Pécourt et je fouille ici pour un cours de journalisme.",
    "From":"pecourt.shannon@courrier.uqam.ca",
}

#Cette ligne va chercher l'information dans l'url.
contenu=requests.get(url, headers=entetes)

#Cette ligne va récupérer le code html de la page
page=BeautifulSoup(contenu.text, "html.parser")

# On crée les listes dont on va avoir besoin dans la boucle en dessous
annee=[]
prod=[]

travaillable1=[]

#Nos données se trouvent dans les cases d'un tableau, qui sont des <td> dans ce code html là. On va donc travailler là dessus.
for ligne in page.find_all("td"):
    # print(ligne.text)
#On transforme les éléments sur lesquels on veut travailler en strings, parce que sinon elles ont un type qui est quelque chose comme "unité BeautifulSoup"
#On en profite pour enlever les espaces et retours à la ligne inutiles (grâce au strip()) et les <td> et </td> (grâce au .text)
    travaillable1.append(str(ligne.text).strip())
    
#Ce qui ne m'intéresse pas, c'est les éléments de 0 à 5, et les 9 éléments de la fin. On les enlève donc de la liste.
travaillable2=travaillable1[6:-9]

#On veut avoir juste une liste avec les années, et un liste avec la production d'électricité de cette année au Canada.
#Il y a des choses qui reviennent à chaque ligne du tableau de façon identique, on dit alors au script de les enlever de la liste quand il les rencontre dans la liste
#Comme "Canada", "Electricity - total hydro production" et "Kilowatt-hours, million" ne changent pas selon les années, on les enlève de notre liste de travail
for chose in travaillable2:
    if chose=="Canada":
        travaillable2.remove(chose)
for chose in travaillable2:
    if chose=="Electricity - total hydro production":
        travaillable2.remove(chose)
for chose in travaillable2:
    if chose=="Kilowatt-hours, million":
        travaillable2.remove(chose)
#On a aussi des éléments vides dans la liste, qu'on retire
for chose in travaillable2:
    if chose=="":
        travaillable2.remove(chose)

# print(travaillable2)
 
#Dans les données qu'on a dans travaillable2, on va séparer les années et le nombre de kw/h
for voulu in travaillable2:
#Pour ça, on va jouer sur le nombre de caractère de l'élément. Une année a toujours 4 caractères, le nombre de kw/h jamais.
    if len(voulu) == 4:
        annee.append(voulu)
    else:
        prod.append(voulu)

# print(annee)
# print(prod)

#La variable ici, c'est le numéro d'index des éléments dans la liste.
for index in range(len(annee)):
#On fait donc varier, en même temps pour qu'elles correspondent, l'année et la production d'éléctricité
    currentannee=annee[index]
    currentprod=prod[index]
    #Tout ça pour afficher cette jolie phrase qui vient terminer le script.
    print("En {}, le Canada a produit {} millions de kilowatts/heure.".format(currentannee,currentprod))
    
#En espérant que ce script vous a plu,
#Have a good day !
