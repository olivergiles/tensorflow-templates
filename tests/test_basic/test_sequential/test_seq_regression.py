from tftemplates.basic_models.sequential_api.binary import main


def test_regression():
    history = main(test=True)
    assert len(history.history["loss"]) == 5
