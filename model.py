import tensorflow as tf

# Residual Block
def residual_block(x, filters):
    shortcut = x

    x = tf.keras.layers.Conv2D(filters, (3,3), padding='same', activation='relu')(x)
    x = tf.keras.layers.Conv2D(filters, (3,3), padding='same')(x)

    if shortcut.shape[-1] != filters:
        shortcut = tf.keras.layers.Conv2D(filters, (1,1), padding='same')(shortcut)

    x = tf.keras.layers.Add()([x, shortcut])
    x = tf.keras.layers.Activation('relu')(x)

    return x

# Build Model
def build_model(input_shape=(128,128,3)):
    inputs = tf.keras.Input(shape=input_shape)

    x = tf.keras.layers.Conv2D(32, (3,3), padding='same', activation='relu')(inputs)

    x = residual_block(x, 32)
    x = tf.keras.layers.MaxPooling2D((2,2))(x)

    x = residual_block(x, 64)
    x = tf.keras.layers.MaxPooling2D((2,2))(x)

    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(128, activation='relu')(x)
    outputs = tf.keras.layers.Dense(1, activation='sigmoid')(x)

    model = tf.keras.Model(inputs, outputs)

    return model