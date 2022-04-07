from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from tensorflow.keras import Model
from tensorflow.keras.layers import Dense

class BasicBinaryModel(Model):
  def __init__(self):
    super().__init__()
    self.dense1 = Dense(8, activation="relu")
    self.dense2 = Dense(1, activation="sigmoid")

  def call(self, inputs):
    x = self.dense1(inputs)
    return self.dense2(x)

def create_model():
    model = BasicBinaryModel()
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


def main(test=False):
    EPOCHS = 500
    if test:
        EPOCHS = 5
    X, y = make_moons(n_samples=250, noise=0.2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    model = create_model()
    history = model.fit(X_train, y_train, epochs=EPOCHS, validation_split=0.3, batch_size=32)
    print(model.evaluate(X_test, y_test))
    return history


if __name__ == "__main__":
    history = main()
    assert len((history.history["loss"])) == 500
