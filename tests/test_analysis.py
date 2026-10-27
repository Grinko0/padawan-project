from padawan_ds.analysis import extract_lemmas

def test_list_lemmas():
    """
    test per verificare che la lista ottenuta coincida con
    quella definita
    """

    gold_lemmas = ["the", "force", "knowledge", "and", "self", "discipline"]
    lemmas = extract_lemmas("The Force, knowledge and self-discipline")
    assert lemmas == gold_lemmas


def test_none_lemmas():
    """
    Test per verificare che le stopwords vengano
    tenute nella fase di analisi
    """
    none_lemma = "none"
    lemmas = extract_lemmas("None.")
    assert none_lemma in lemmas