import tensorflow as tf

def main():
    mirrored_strategy = tf.distribute.MirroredStrategy()

    with mirrored_strategy.scope():
      model = tf.keras.Sequential([tf.keras.layers.Dense(1, input_shape=(1,))])
    
    model.compile(loss='mse', optimizer='sgd')
    dataset = tf.data.Dataset.from_tensors(([1.], [1.])).repeat(100).batch(10)
    model.fit(dataset, epochs=2)
    model.evaluate(dataset)

if __name__ == "__main__":
    main()
