import webbrowser
from urllib.parse import quote_plus

# --------------------------------------------------
GITHUB_USER = "Xinye-Star-Yu"
REPO        = "Alphafold_CryoID"
BRANCH      = "main"
NB_PATH     = "notebooks/AlphaFold2.ipynb"
# --------------------------------------------------

colab_url = (
    "https://colab.research.google.com/github/"
    f"{quote_plus(GITHUB_USER)}/{quote_plus(REPO)}/blob/"
    f"{quote_plus(BRANCH)}/{quote_plus(NB_PATH)}"
)

print("Opening ColabFold…")
webbrowser.open(colab_url, new=2)   # new=2 → new tab, if possible
