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
# "Poème de" "Poème" "Année" "Ref SACEM" "date SACEM" "note max" "Editeur" 
#"Extrait" "Partition<br>éditée" "Partition<br>manuscrite" 
usecols = ["n°opus","titre","Genre","Poème","Instruments","Extrait","Partition<br>éditée", "Partition<br>manuscrite","Année"]


def partitionGraveeURL(u):
    return f'<a href="../partitions/GraveOuEdite/{u}" target="_blank">PDF</a>'
def partitionManuscriteURL(u):
    return f'<a href="../partitions/Manuscrit/{u}" target="_blank">PDF</a>'
def extraitURL(u):
    return f'<a href="../extraits/{u}" target="_blank">&#9835;</a>'
def poemeURL(u):
    return f'<a href="{u}" target="_blank">poème</a>'
   

def lire_formater_catalogue():
	
  options.warn_on_undocumented_option = False
  # Charger le fichier CSV
  df = pd.read_csv(csvfile, index_col=1, usecols=usecols)
  #df = pd.read_csv("CatalogueGeorgesTaconet.csv", index_col=1, usecols=usecols)
  df["Partition<br>éditée"]=df["Partition<br>éditée"].apply(lambda u:  '/' if pd.isna(u) else partitionGraveeURL(u))

  df["Année"] = df["Année"].astype("Int64").astype(str).apply(lambda u:  '?' if pd.isna(u) else u)
  df["Partition<br>manuscrite"]=df["Partition<br>manuscrite"].apply(lambda u: '/' if pd.isna(u) else partitionManuscriteURL(u))
  df["Extrait"]=df["Extrait"].apply(lambda u: '/' if pd.isna(u) else extraitURL(u))
  df["Poème"]=df["Poème"].apply(lambda u: '/' if pd.isna(u) else poemeURL(u))

# html possible
  df.to_html(classes="table",escape=False, index=False)
  df_filtre_soprano = df[df["Instruments"].str.contains("soprano")]
  df_filtre_piano = df[df["Instruments"]=="piano"]
  return df;
  
def filtrer_catalogue(df, filtre):
  match filtre:
    case "voix":
      df = df[df["Genre"].str.contains("Mélodie|Mélodie|Ensemble vocal",case=False,na=False)]
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
      df = df.drop(columns=["Poème"])
      return df
    case "piano":
      df = df[df["Instruments"]=="piano"]
      df = df.drop(columns=["Genre"])
      df = df.drop(columns=["Poème"])
      return df
    case "orgue":
      df = df[df["Instruments"].str.contains("orgue")]
      df = df.drop(columns=["Genre"])
      df = df.drop(columns=["Poème"])
      return df
    case "harmonium":
      df = df[df["Instruments"].str.contains("harmonium")]
      df = df.drop(columns=["Genre"])
      df = df.drop(columns=["Poème"])
      return df
    case "musique de chambre":
      df = df[df["Genre"].str.contains("Musique de chambre|Orchestre",case=False,na=False)]
      df = df.drop(columns=["Genre"])
      return df
    case "violon":
      df = df[df["Instruments"].str.contains("violon|alto",case=False,na=False)]
      df = df.drop(columns=["Genre"])
      df = df.drop(columns=["Poème"])
      return df
    case "violoncelle":
      df =  df[df["Instruments"].str.contains("violoncelle")]
      df = df.drop(columns=["Genre"])
      df = df.drop(columns=["Poème"])
      return df

# Paramètres pour le show
    # columnControl=["order", "colVisDropdown", "searchDropdown"],
    # paging=False
def afficher_catalogue(df):
  #df = df.reset_index(drop=True)
  html = """
  <div class="catalogue-wrapper">
  """
  display(HTML(html))

  show(df, searchable=True, sortable=True, allow_html=True,columnControl=["order", "colVisDropdown", "searchDropdown"])
  html = """
<p><br><br>* Les partitions manuscrites ne portent pas de date, les dates mentionnées sont soit celles de dépôt à la SACEM, 
pour les oeuvres déposées à la SACEM, soit viennent de la mention de l'oeuvre dans une correspondance.</p>

<p>J'ai rassemblé ici les poèmes mis en musique par Georges TACONET. 
Ils sont présentés dans l'ordre du catalogue, c'est à dire suivant l'ordre alphabétique des poè­tes. 
Il eut été intéressant de connaître la date de composi­tion de chacun d'eux, 
ne serait-ce que pour voir l'évolution dans le temps de l'inspiration du musicien. 
Nous n'avons pas ces dates, mais nous avons quelques indications sur certaines œuvres, 
en tenant compte de la date d'une pre­mière audition, de la date d'inscription à la SACEM, 
ou même de l'écriture du manuscrit.

On peut noter que le jeune compositeur a pris quelques (rares) libertés avec le texte des poésies 
qu’il mettait en musique (voir annotations en bas de page).
</p>
<p>
Signalons que certains de ces poèmes ont inspiré d’autres musiciens :
<ul>
<li>Gabriel Fauré (Soir, d’Albert Samain ; Au bord de l’eau, de Sully Prud’homme ; Tous deux, de Verlaine)</li>
<li>E. Chausson (Dans la forêt chauve et rouillée, de Théophile Gautier)</li>
<li>Cl. Debussy (Rondel, de Charles d’Orléans)</li>
</ul>
Je me fais un devoir et un plaisir de remercier ici Mme Mauricette Vinay. 
Fille de Blanche Vinay-Leconte, violoniste de grand talent, très appréciée de Georges Taconet, 
et elle même agrégée de lettres, elle m’a signalé et évité bien des fautes de frappe ou de prosodie. 
En outre elle a rédigé l’essentiel des deux pages qui suivent : Situons les Poètes.
</p>
<p>
Henri Taconet
</br>
avril 1998-juin 200
</p>
</div>
"""

  display(HTML(html))
  