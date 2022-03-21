import seaborn as sns

from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Normalization


def create_model():
    """Basic regression prediction model with the sequential API"""
    model = Sequential(
        [
            Normalization(input_dim=1),
            Dense(5, activation="relu"),
            Dense(1, activation="linear"),
        ]
    )
    model.compile(loss="mse", optimizer="adam", metrics=["mse"])
    return model


def main(test=False):
    EPOCHS = 500
    if test:
        EPOCHS = 5
    df = sns.load_dataset("diamonds")
    X = df[["carat"]].copy()
    y = df["price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    model = create_model()
    history = model.fit(
        X_train, y_train, epochs=EPOCHS, validation_split=0.3, batch_size=32
    )
    print(model.evaluate(X_test, y_test))
    return history


if __name__ == "__main__":
    history = main()
    assert len(history.history["loss"]) == 500
