---
jupyter:
  kernelspec:
    display_name: "Python 3"
    language: "python"
    name: "python3"
---


# Entendre la musique

```{figure} ../musique/jaquetteNaxos.gif 
:alt: 
:width:
:align: left

```

On peut entendre des mélodies et la sonate en ré bémol mineur (pour violon et piano) sur un [CD](https://www.naxos.com/catalogue/item.asp?item_code=8.225300) édité par Naxos Marco Polo.

Vous pouvez écouter les morceaux musicaux du disque Naxos sur youtube ([la sonate piano violon]("https://www.youtube.com/results?search_query=georges+taconet+fanny+clamagirand) et [les mélodies](https://www.youtube.com/results?search_query=georges+taconet+dominique+mea)).

```{figure} ../photos/SensbachBoydYoutube.png
:alt: 
:width: 300
:align: left

```

Vous pouvez écouter la sonate pour violoncelle et piano opus 83 en mi bémol majeur, Stephen SENSBACH, violoncelle et Kate BOYD, piano : [1 Allegro moderato](https://www.youtube.com/watch?v=WMEClKWkJGk), [2 Andante](https://www.youtube.com/watch?v=iv9WOXPPFWw), [3 Allegro deciso](https://www.youtube.com/watch?v=5BlTjP_DWUQ)


D'autres extraits sont accessibles ci-dessous. 

- La *sonate en lab M* est interprétée au piano par Dominique Sevet. 
- *Danse comme les autres*, *Dernières lueurs sur la mer*, *Impression d'été*, *Jeux d'enfants*, *Valse*, sont interprétées au piano par Kate Boyd (enregistrées en 2003). 
- Les mélodies pour soprano et piano sont des extraits du disque Naxos interprétés par Dominique Méa (soprano) et Carlos Cebro au piano. 
- Le *quintette* a été enregistré à Sainte Adresse en 2003 autour du pianiste Olivier Cangelosi


```{code-cell} python
:tags: [remove-input]
from outils.catalogue import lire_formater_catalogue
from outils.catalogue import filtrer_catalogue
from outils.catalogue import afficher_catalogue

df=lire_formater_catalogue()
df=filtrer_catalogue(df,"extraits")
afficher_catalogue(df)
```
