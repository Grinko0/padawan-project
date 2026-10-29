from padawan_ds.analysis import extract_lemmas, fill_slots

# Slot della domanda sui pilastri, scritti qui per rendere i test
# indipendenti dalla knowledge base: se il JSON cambia, questi test
# continuano a verificare solo la logica di fill_slots.
PILLARS_SLOTS = {
    "force": ["force"],
    "knowledge": ["knowledge", "wisdom"],
    "self_discipline": ["discipline"],
}


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

def test_fill_slots_partial_answer():
    """Una risposta parziale riempie solo gli slot nominati (Trindi Q4)."""
    lemmas = ["the", "force", "and", "wisdom"]
    assert fill_slots(lemmas, PILLARS_SLOTS) == {"force", "knowledge"}


def test_fill_slots_unrelated_answer():
    """Una risposta fuori tema non riempie nessuno slot."""
    lemmas = ["i", "like", "apple"]
    assert fill_slots(lemmas, PILLARS_SLOTS) == set()


def test_fill_slots_complete_answer():
    """Una risposta completa riempie tutti gli slot della domanda."""
    lemmas = ["the", "force", "knowledge", "and", "self", "discipline"]
    assert fill_slots(lemmas, PILLARS_SLOTS) == set(PILLARS_SLOTS)