from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Normalization
from tensorflow.keras.utils import to_categorical


def create_model():
    model = Sequential(
        [Normalization(input_dim=8),
        Dense(50, activation="relu"),
        Dense(7, activation="softmax")]
    )
    model.compile(loss='categorical_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])
    return model

def main(test=False):
    EPOCHS = 500
    if test:
        EPOCHS = 3
    X, y = make_blobs(500, 8, centers=7, cluster_std=8,random_state=42)
    y_cat = to_categorical(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y_cat)
    model = create_model()
    history = model.fit(X_train, y_train, epochs=500, validation_split=0.3, batch_size=32)
    return history

if __name__ == "__main__":
    history = main()
    assert(len(history.history) == 500)