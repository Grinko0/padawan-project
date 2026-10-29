import spacy
# in questo file carico il modello spaCy che utilizzo per estrarre
# i lemmi da una frase che viene data in input dall'utente

NLP = spacy.load("en_core_web_sm")

def extract_lemmas(text: str) -> list[str]:
    """
    restituisce i lemmi normalizzati, in minuscolo
     per il confronto con gli slots e le stopword
     vengono tenute perchè le negazioni sono importanti
     tipo not o none.
    """
    doc = NLP(text)
    cleaned_lemmas = [token.lemma_.lower() for token in doc if not token.is_punct 
                      and not token.is_space]

    return cleaned_lemmas


def fill_slots(lemmas: list[str], slots: dict[str, list[str]]) -> set[str]:
    """
    Riceve i lemmi della risposta e il dizionario degli slot della 
    domanda e restituisce un set dei nomi degli slot che sono stati
    riempiti
    """
    filled_slots = set()

    for slot_name, slot_lemmas in slots.items():
        is_slot_filled = any(lemma in lemmas for lemma in slot_lemmas)
        if is_slot_filled:
            filled_slots.add(slot_name)

    return filled_slots