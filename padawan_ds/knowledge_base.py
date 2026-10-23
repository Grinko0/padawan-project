import json
from pathlib import Path
import os

# trasforma in oggetto Path il percorso. resolve() lo rende assoluto e parent
# risale a padawan_ds il secondo invece alla radice del progetto.
DEFAULT_KB_PATH = Path(__file__).resolve().parent.parent / "data" / "jedi_kb.json"

def load_questions(path: str | os.PathLike = DEFAULT_KB_PATH) -> list[dict]:
    """
    funzione che prende in input un percorso
    e restituisce la lista delle domande
    della knowledge base. 
    """
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    questions = data["questions"]

    return questions