---
jupyter:
  kernelspec:
    display_name: "Python 3"
    language: "python"
    name: "python3"
---

# Catalogue des œuvres


```{code-cell} python
:tags: [remove-input]
from outils.catalogue import lire_formater_catalogue
from outils.catalogue import filtrer_catalogue
from outils.catalogue import afficher_catalogue


df=lire_formater_catalogue()
afficher_catalogue(df)
```
