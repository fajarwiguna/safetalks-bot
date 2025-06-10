import tensorflow as tf
import pickle

# Register layer & loss
@tf.keras.utils.register_keras_serializable()
class SimpleAttention(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super(SimpleAttention, self).__init__(**kwargs)
    def build(self, input_shape):
        self.kernel = self.add_weight(name="kernel", shape=(input_shape[-1], 1), initializer="glorot_uniform", trainable=True)
        self.bias = self.add_weight(name="bias", shape=(input_shape[1], 1), initializer="zeros", trainable=True)
        super(SimpleAttention, self).build(input_shape)
    def call(self, inputs):
        e = tf.keras.backend.tanh(tf.tensordot(inputs, self.kernel, axes=1) + self.bias)
        alpha = tf.keras.backend.softmax(e, axis=1)
        context = tf.reduce_sum(alpha * inputs, axis=1)
        return context

@tf.keras.utils.register_keras_serializable()
def focal_loss_fn(y_true, y_pred, gamma=2.0, alpha=0.25):
    y_true = tf.cast(y_true, tf.float32)
    epsilon = tf.keras.backend.epsilon()
    y_pred = tf.clip_by_value(y_pred, epsilon, 1. - epsilon)
    cross_entropy = -y_true * tf.math.log(y_pred)
    weight = alpha * tf.pow(1 - y_pred, gamma)
    loss = weight * cross_entropy
    return tf.reduce_sum(loss, axis=1)

# Load model & tokenizer
with open('model/tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = tf.keras.models.load_model('model/lstm_model.keras')
