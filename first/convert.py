import keras


def custom_batch_norm(config):
    if 'axis' in config and isinstance(config['axis'], list):
        config['axis'] = config['axis'][0]
    return keras.models.BatchNormalization(**config)

custom_objects = {'BatchNormalization': custom_batch_norm}

model_path = r"D:\VS projects\first\Model2.h5"
model = keras.models.load_model(model_path, custom_objects=custom_objects)
#model = keras.models.load_model(r"D:\VS projects\first\Model2.h5")
model.save("Model.keras")