from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential


def create_model():
    """Most basic binary classification model wit the sequential api"""
    model = Sequential(
        [Dense(8, activation="relu", input_dim=2), Dense(1, activation="sigmoid")]
    )
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


def main(test=False):
    EPOCHS = 500
    if test:
        EPOCHS = 5
    X, y = make_moons(n_samples=250, noise=0.2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    model = create_model()
    history = model.fit(X_train, y_train, epochs=5, validation_split = 0.3, batch_size = 32)
    print(model.evaluate(X_test, y_test))
    return history


if __name__ == "__main__":
    history = main()
    assert len((history.history["loss"])) == 500
