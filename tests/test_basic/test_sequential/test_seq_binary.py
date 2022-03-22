from tftemplates.basic_models.sequential_api.binary import main


def test_binary():
    history = main(test=True)
    assert len((history.history["loss"])) == 5
