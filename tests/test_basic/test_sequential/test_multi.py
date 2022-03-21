from re import L
from tftemplates.basic_models.sequential_api.multi import main


def test_multi():
    history = main(test=True)
    assert len(history.history["loss"]) == 5
