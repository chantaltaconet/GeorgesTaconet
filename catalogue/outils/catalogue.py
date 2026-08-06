import pandas as pd
from IPython.display import HTML, display
from itables import show
from itables import options
from IPython.display import display, HTML

options.language = {
    "url": "https://cdn.datatables.net/plug-ins/1.13.8/i18n/fr-FR.json"
}
csvfile="CatalogueGeorgesTaconet_pourJupyterBook.csv"
#usecols à choisir parmi "n°opus" "titre" "nb de pages"	"Genre" "Instruments" "durée<br>en mn" 
# "Poème de" "Poème<br>Texte" "Année" "Ref SACEM" "date SACEM" "note max" "Editeur" 
#"Extrait" "Partition<br>éditée" "Partition<br>manuscrite" 
usecols = ["n°opus","titre","Genre","Poème<br>Texte","Instruments","Extrait","Partition<br>éditée", "Partition<br>manuscrite","Année"]
symboleextrait="&#9836;"

def partitionGraveeURL(u):
    return f'<a href="../partitions/GraveOuEdite/{u}" target="_blank">PDF</a>'
def partitionManuscriteURL(u):
    return f'<a href="../partitions/Manuscrit/{u}" target="_blank">PDF</a>'
def extraitURL(u):
    return f'<a href="../extraits/{u}" target="_blank"><b> <font size="+4">&#9836;</font></b></a>'
def poemeURL(u):
    return f'<a href="../{u}" target="_blank">Texte</a>'
   

def lire_formater_catalogue():
	
  options.warn_on_undocumented_option = False
  # Charger le fichier CSV
  df = pd.read_csv(csvfile, index_col=1, usecols=usecols)
  #df = pd.read_csv("CatalogueGeorgesTaconet.csv", index_col=1, usecols=usecols)
  df["Partition<br>éditée"]=df["Partition<br>éditée"].apply(lambda u:  '/' if pd.isna(u) else partitionGraveeURL(u))

  df["Année"] = df["Année"].astype("Int64").astype(str).apply(lambda u:  '?' if pd.isna(u) else u)
  df["Partition<br>manuscrite"]=df["Partition<br>manuscrite"].apply(lambda u: '/' if pd.isna(u) else partitionManuscriteURL(u))
  df["Extrait"]=df["Extrait"].apply(lambda u: '/' if pd.isna(u) else extraitURL(u))
  df["Poème<br>Texte"]=df["Poème<br>Texte"].apply(lambda u: '/' if pd.isna(u) else poemeURL(u))

# html possible
  df.to_html(classes="table",escape=False, index=False)
  df_filtre_soprano = df[df["Instruments"].str.contains("soprano")]
  df_filtre_piano = df[df["Instruments"]=="piano"]
  return df;
  
def filtrer_catalogue(df, filtre):
  match filtre:
    case "voix":
      df = df[df["Genre"].str.contains("Mélodie|Religieuse|Ensemble vocal",case=False,na=False)]
      df = df.drop(columns=["Genre"])
      return df
    case "mélodie":
      df = df[df["Genre"].str.contains("Mélodie")]
      df = df.drop(columns=["Genre"])
      return df
    case "ensemble vocal":
      df = df[df["Genre"].str.contains("Ensemble vocal")]
      df = df.drop(columns=["Genre"])
      return df
    case "musique religieuse":
      df = df[df["Genre"].str.contains("Religieuse")]
      df = df.drop(columns=["Genre"])
      return df
    case "clavier":
      df = df[df["Instruments"].str.contains("piano|orgue|harmonium",case=False,na=False)]
      df = df.drop(columns=["Genre"])
      df = df.drop(columns=["Poème<br>Texte"])
      return df
    case "piano":
      df = df[df["Instruments"]=="piano"]
      df = df.drop(columns=["Genre"])
      df = df.drop(columns=["Poème<br>Texte"])
      return df
    case "orgue":
      df = df[df["Instruments"].str.contains("orgue")]
      df = df.drop(columns=["Genre"])
      df = df.drop(columns=["Poème<br>Texte"])
      return df
    case "harmonium":
      df = df[df["Instruments"].str.contains("harmonium")]
      df = df.drop(columns=["Genre"])
      df = df.drop(columns=["Poème<br>Texte"])
      return df
    case "musique de chambre":
      df = df[df["Genre"].str.contains("Musique de chambre|Orchestre",case=False,na=False)]
      df = df.drop(columns=["Genre"])
      return df
    case "orchestre":
      df = df[df["Genre"].str.contains("Orchestre",case=False,na=False)]
      df = df.drop(columns=["Genre"])
      return df
    case "violon":
      df = df[df["Instruments"].str.contains("violon|alto",case=False,na=False)]
      df = df.drop(columns=["Genre"])
      df = df.drop(columns=["Poème<br>Texte"])
      return df
    case "violoncelle":
      df =  df[df["Instruments"].str.contains("violoncelle")]
      df = df.drop(columns=["Genre"])
      df = df.drop(columns=["Poème<br>Texte"])
      return df
    case "extraits":
      df = df[df["Extrait"].str.contains(symboleextrait)]
      df = df.drop(columns=["Genre"])
      df = df.drop(columns=["Partition<br>éditée"])
      df = df.drop(columns=["Partition<br>manuscrite"])
      df = df.drop(columns=["Année"])
      df = df.drop(columns=["Poème<br>Texte"])
      return df


# Paramètres pour le show
    # columnControl=["order", "colVisDropdown", "searchDropdown"],
    # paging=False
def afficher_catalogue(df):
  #df = df.reset_index(drop=True)

  show(df, searchable=True, sortable=True, allow_html=True,columnControl=["order", "colVisDropdown", "searchDropdown"])

def afficher_commentaire():  
  html = """
<p><br><br>* Les partitions manuscrites ne portent pas de date, les dates mentionnées sont soit celles de dépôt à la SACEM, 
pour les oeuvres déposées à la SACEM, soit viennent de la mention de l'oeuvre dans une correspondance.</p>


<blockquote>
<p><i>J'ai rassemblé ici les poèmes mis en musique par Georges TACONET. 
Ils sont présentés dans l'ordre du catalogue, c'est à dire suivant l'ordre alphabétique des poè­tes. 
Il eut été intéressant de connaître la date de composi­tion de chacun d'eux, 
ne serait-ce que pour voir l'évolution dans le temps de l'inspiration du musicien. 
Nous n'avons pas ces dates, mais nous avons quelques indications sur certaines œuvres, 
en tenant compte de la date d'une pre­mière audition, de la date d'inscription à la SACEM, 
ou même de l'écriture du manuscrit.</i>
</p>
</blockquote> - Henri Taconet Juin 2000
"""

  display(HTML(html))
  