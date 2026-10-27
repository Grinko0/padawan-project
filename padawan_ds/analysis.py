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

