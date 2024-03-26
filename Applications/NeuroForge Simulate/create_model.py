import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.models import Model

def create_model(input_shape, num_classes):
    inputs = Input(shape=input_shape)
    x = Conv2D(32, (3, 3), activation='relu', padding='same')(inputs)
    x = MaxPooling2D((2, 2), padding='same')(x)
    x = Conv2D(64, (3, 3), activation='relu', padding='same')(x)
    x = MaxPooling2D((2, 2), padding='same')(x)
    x = Flatten()(x)
    x = Dense(128, activation='relu')(x)
    outputs = Dense(num_classes, activation='softmax')(x)
    model = Model(inputs=inputs, outputs=outputs)
    return model

# Define input shape and number of classes
input_shape = (28, 28, 1)
num_classes = 10

# Create the model
model = create_model(input_shape, num_classes)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Load training data
train_data = ...

# Load test data
test_data = ...

# Train the model
model.fit(train_data, epochs=10, validation_data=test_data)

# Evaluate the model
loss, accuracy = model.evaluate(test_data)
print('Test accuracy: {:.2f}%'.format(accuracy * 100))

# Simulate different neural network architectures and configurations
# Example: Change the number of filters in the first convolutional layer
model = create_model(input_shape, num_classes)
model.layers[1].filters = 64
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_data, epochs=10, validation_data=test_data)
