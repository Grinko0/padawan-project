import spacy 

MODEL_NAME = "en_core_web_sm"

def test_load_model():
    """
    funzione di test per verificare
    se il modello viene caricato
    correttamente
    """

    # carico il modello e ottengo un oggetto Language
    # ovvero una pipeline per elaborare il testo 
    # a cui posso passare una stringa per fare 
    # determinate analisi
    nlp = spacy.load(MODEL_NAME)

    # verifico che siano presenti le componenti come il parser
    # e il lemmatizer all'interno dell'oggetto Language.
    assert "parser" in nlp.pipe_names
    assert "lemmatizer" in nlp.pipe_names

    # lingua inglese
    assert nlp.lang== "en"


def test_negation_detected():
    """
    Verifica che il parser marchi la negazione con la relazione 'neg'.
    L'analisi delle risposte dell'utente si basa su questa etichetta per
    capire cosa viene negato: se cambiasse modello o parser (es. Stanza,
    che usa advmod + Polarity=Neg), questo test segnalerebbe che la logica
    di analisi va adattata.
    """

    nlp = spacy.load(MODEL_NAME)
    # ottengo un oggetto Doc cje contiene una sequenza di token
    # che contiene informazioni riguardo al POS tagging, lemmatizzazione
    # e altre...
    doc = nlp("Jedi can't have children")

    # per ogni token stampo testo, relazione e la head
    # e verifico che ci sia un token per la negazione con dep_ == "neg"
    for token in doc:
        print(f"Token: {token.text}. Relation: {token.dep_}. Head: {token.head.text}")

    # utilizzo la funzione any() che verifica se è presente almeno 
    # un token di negazione nella frase e restituisce un booleano
    assert any(token.dep_ == "neg" for token in doc)
        




