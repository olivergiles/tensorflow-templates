from tftemplates.basic_models.functional_api.multi import main


def test_multi():
    history = main(test=True)
    assert len(history.history["loss"]) == 5
