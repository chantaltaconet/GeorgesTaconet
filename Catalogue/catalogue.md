---
jupyter:
  kernelspec:
    display_name: "Python 3"
    language: "python"
    name: "python3"
---

# Catalogue des oeuvres


```{code-cell} python
:tags: [remove-input]
from itables import show
from itables import options
from IPython.display import display, HTML

options.warn_on_undocumented_option = False
import pandas as pd

def partitionGraveeURL(u):
    return f'<a href="./partitions/GraveOuEdite/{u}" target="_blank">PDF</a>'
def partitionManuscriteURL(u):
    return f'<a href="./partitions/Manuscrit/{u}" target="_blank">PDF</a>'

# Defining the columns to read
usecols = ["n°opus","titre","Genre","Instruments","Partition<br>éditée", "Partition<br>manuscrite","Année"]

# Charger le fichier CSV
df = pd.read_csv("CatalogueGeorgesTaconet_pourJupyterBook.csv", index_col=1, usecols=usecols)
#df = pd.read_csv("CatalogueGeorgesTaconet.csv", index_col=1, usecols=usecols)
df["Partition<br>éditée"]=df["Partition<br>éditée"].apply(lambda u:  '/' if pd.isna(u) else partitionGraveeURL(u))

df["Année"] = df["Année"].astype("Int64").astype(str).apply(lambda u:  'Inconnue' if pd.isna(u) else u)
df["Partition<br>manuscrite"]=df["Partition<br>manuscrite"].apply(lambda u: '/' if pd.isna(u) else partitionManuscriteURL(u))

# html possible
df.to_html(classes="table",escape=False, index=False)
df_filtre_soprano = df[df["Instruments"].str.contains("soprano")]
df_filtre_piano = df[df["Instruments"]=="piano"]
```
## Toutes les oeuvres
```{code-cell} python
:tags: [remove-input]

show(df, searchable=True, sortable=True, allow_html=True)

## Pièces pour soprano 
```
## Oeuvres pour soprano
```{code-cell} python
:tags: [remove-input]

show(df_filtre_soprano, searchable=True, sortable=True, allow_html=True)

```
## Pièces pour piano
```{code-cell} python
:tags: [remove-input]

show(df_filtre_piano, searchable=True, sortable=True, allow_html=True)

```

