import pandas as pd
from IPython.display import HTML, display


def afficher_liens_par_categorie(fichier_csv):

    # Lecture du CSV
    df = pd.read_csv(
        fichier_csv,
        sep=",",
        encoding="utf-8"
    )

    html = ""

    # Tri par catégorie puis par nom
    df = df.sort_values(["categorie", "nom"])

    # Création des groupes
    for categorie, groupe in df.groupby("categorie"):

        html += f"""
        <h2 class="liens-categorie">
            {categorie}
        </h2>
        """

        html += '<ul class="liens-liste">'

        for _, ligne in groupe.iterrows():

            html += f"""
            <li class="liens-item">
                <a href="{ligne['url']}"
                   target="_blank"
                   rel="noopener noreferrer"
                   class="liens-url">
                   {ligne['nom']}
                </a>
            </li>
            """

        html += "</ul>"

    display(HTML(html))
