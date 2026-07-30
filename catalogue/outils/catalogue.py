import pandas as pd
from IPython.display import HTML, display
from itables import show
from itables import options
from IPython.display import display, HTML

options.language = {
    "url": "https://cdn.datatables.net/plug-ins/1.13.8/i18n/fr-FR.json"
}
csvfile="CatalogueGeorgesTaconet_pourJupyterBook.csv"

def partitionGraveeURL(u):
    return f'<a href="../partitions/GraveOuEdite/{u}" target="_blank">PDF</a>'
def partitionManuscriteURL(u):
    return f'<a href="../partitions/Manuscrit/{u}" target="_blank">PDF</a>'

#usecols à choisir parmi "n°opus" "titre" "nb de pages"	"Genre" "Instruments" "durée<br>en mn" 
# "Poème de" "Poème" "Année" "Ref SACEM" "date SACEM" "note max" "Editeur" 
#"Extrait" "Partition<br>éditée" "Partition<br>manuscrite" 
def lire_formater_catalogue(usecols):
	
  options.warn_on_undocumented_option = False
  # Charger le fichier CSV
  df = pd.read_csv(csvfile, index_col=1, usecols=usecols)
  #df = pd.read_csv("CatalogueGeorgesTaconet.csv", index_col=1, usecols=usecols)
  df["Partition<br>éditée"]=df["Partition<br>éditée"].apply(lambda u:  '/' if pd.isna(u) else partitionGraveeURL(u))

  df["Année"] = df["Année"].astype("Int64").astype(str).apply(lambda u:  '?' if pd.isna(u) else u)
  df["Partition<br>manuscrite"]=df["Partition<br>manuscrite"].apply(lambda u: '/' if pd.isna(u) else partitionManuscriteURL(u))

# html possible
  df.to_html(classes="table",escape=False, index=False)
  df_filtre_soprano = df[df["Instruments"].str.contains("soprano")]
  df_filtre_piano = df[df["Instruments"]=="piano"]
  return df;
  
def filtrer_catalogue(df, filtre):
  match filtre:
    case "piano":
      df = df.drop(columns=["Genre"])
      return df[df["Instruments"]=="piano"]
   
# Paramètres pour le show
    # columnControl=["order", "colVisDropdown", "searchDropdown"],
    # paging=False
def afficher_catalogue(df):
  show(df, searchable=True, sortable=True, allow_html=True,columnControl=["order", "colVisDropdown", "searchDropdown"])
  html = """
<p><br><br>* Les partitions manuscrites ne portent pas de date, les dates mentionnées sont soit celles de dépôt à la SACEM, 
pour les oeuvres déposées à la SACEM, soit viennent de la mention de l'oeuvre dans une correspondance.</p>
"""

  display(HTML(html))
  