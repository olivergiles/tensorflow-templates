from tftemplates.basic_models.inhertiance.binary import main


def test_binary():
    history = main(test=True)
    assert len((history.history["loss"])) == 5
