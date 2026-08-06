---
jupyter:
  kernelspec:
    display_name: "Python 3"
    language: "python"
    name: "python3"
---

# Mélodies


```{code-cell} python
:tags: [remove-input]
from outils.catalogue import lire_formater_catalogue
from outils.catalogue import filtrer_catalogue
from outils.catalogue import afficher_catalogue
from outils.catalogue import afficher_commentaire

df=lire_formater_catalogue()
df=filtrer_catalogue(df,"mélodie")
afficher_catalogue(df)
afficher_commentaire()
```
