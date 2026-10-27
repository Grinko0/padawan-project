from padawan_ds.knowledge_base import load_questions
# quando faccio l'import, importo sia la funzione che il suo valore
# di default. 

def test_questions_no_empty_list():
    """
    Test per verificare che la lista
    non sia vuota
    """
    questions = load_questions()
    assert isinstance(questions,list)
    assert len(questions) > 0


def test_questions_keys():
    """
    Verifico che in ogni domanda ci siano
    le chiavi: id, text, slots.
    """
    questions = load_questions()

    for question in questions:
        qid = question.get("id")
        assert "id" in question, f"A question is missing the 'id' key: {question}"
        assert "text" in question, f"Question '{qid}' is missing the 'text' key"
        assert "slots" in question, f"Question '{qid}' is missing the 'slots' key"


def test_lower_lemmas():
    """
    i lemmi in ogni slot di domanda
    devo essere minuscoli
    """
    questions = load_questions()

    for question in questions: # dict
        for lemmas in question["slots"].values(): # list
            for lemma in lemmas: # string
                assert lemma == lemma.lower(), f"The lemma {lemma} must be lowercase"
        

