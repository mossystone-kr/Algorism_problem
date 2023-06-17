import tensorflow as tf

print(tf.__version__)
print(tf.version.VERSION)
print(tf.version.GIT_VERSION)
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))