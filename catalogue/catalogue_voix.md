---
jupyter:
  kernelspec:
    display_name: "Python 3"
    language: "python"
    name: "python3"
---

# Œuvres pour voix


```{code-cell} python
:tags: [remove-input]
from outils.catalogue import lire_formater_catalogue
from outils.catalogue import filtrer_catalogue
from outils.catalogue import afficher_catalogue

usecols = ["n°opus","titre","Genre","Instruments","Partition<br>éditée", "Partition<br>manuscrite","Année"]
df=lire_formater_catalogue(usecols)
df=filtrer_catalogue(df,"voix")
afficher_catalogue(df)
```
