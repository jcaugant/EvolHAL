#!/usr/bin/env python
# coding: utf-8

# In[15]:

import requests as rq, json, matplotlib.pyplot as plt, numpy as np
nb_notice, nb_text, nb_annex, date_hal = [], [], [], []
collection = input("Entrez l'acronyme du portail ou de la collection sur lequel faire l'analyse : ")
start_y = int(input("Rentrez une année de départ pour votre analyse : "))
end_y = int(input("Rentrez une année de fin pour votre analyse : "))
for year in range (start_y, end_y+1) : 
    for month in range(1, 13) : 
        url = f"https://api.archives-ouvertes.fr/search/{collection}/?rows=0&fq=submittedDateY_i:{year}&fq=submittedDateM_i:{month}&facet=true&facet.field=submitType_s"
        req = rq.get(url)
        req = req.json()
        notice = req["facet_counts"]["facet_fields"]["submitType_s"][1]
        fichier = req["facet_counts"]["facet_fields"]["submitType_s"][3]
        annexe = req["facet_counts"]["facet_fields"]["submitType_s"][5]
        date = f"{year}-{month}"
        nb_notice.append(notice)
        nb_text.append(fichier)
        nb_annex.append(annexe)
        date_hal.append(date)    
# plt.plot_date(2018,2022, xdate=True)
plt.figure(figsize=(20, 5))
plt.plot(nb_text,"b", label="Texte intégral")
plt.plot(nb_notice,"r", label="Notice")
plt.plot(nb_notice,"y", label="Annexe")
plt.title("Evolution des dépôts en texte intégral dans HAL")
plt.xlabel('Date')
plt.xticks(range(len(date_hal)), date_hal, rotation=45)
plt.ylabel('Nombre de dépôts')
plt.legend()
print("Le nombre maximum de notices déposés est de :", max(nb_notice), "sur un mois")
print("Le nombre maximum de dépôts avec texte est de :", max(nb_text), "sur un mois")
print("Le nombre maximum d'annexes déposées est de :", max(nb_annex), "sur un mois")
print("En moyenne, votre structure dépose :", sum(nb_text) / len(nb_text), "par mois")
