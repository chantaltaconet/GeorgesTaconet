import pandas as pd
from itables import show
from IPython.display import HTML, display
def afficher_liens_par_categorie(fichier_csv):

    # Lecture du CSV
    df = pd.read_csv(
        fichier_csv,
        sep=",",       # ton exemple est séparé par tabulation
        encoding="utf-8"
    )

    html = ""

    # Tri par catégorie puis par nom
    df = df.sort_values(["categorie", "nom"])

    # Création des groupes
    for categorie, groupe in df.groupby("categorie"):

        html += f"""
        <h2 style="
            color:#181876;
            margin-top:30px;
            border-bottom:2px solid #181876;
            padding-bottom:5px;">
            {categorie}
        </h2>
        """

        html += "<ul>"

        for _, ligne in groupe.iterrows():

            html += f"""
            <li style="margin-bottom:8px;">
                <a href="{ligne['url']}" 
                   target="_blank"
                   style="color:#181876;">
                   {ligne['nom']}
                </a>
            </li>
            """

        html += "</ul>"

    display(HTML(html))