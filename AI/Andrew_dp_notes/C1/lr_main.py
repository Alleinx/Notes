# This program bulids a Logistic regression classifier to recognize cats.

# Import packages
# ---------------
import numpy as np
import matplotlib.pyplot as plt
import h5py
# h5py is a common package to interact with a dataset that is stored on an H5 file
from PIL import Image
from scipy import ndimage
import lr_utils 

# Load the data:
# -------------
# We add '_orig' at the end of the image datasets because we are going to preprocess
# them. After preprocessing, we will end up with train_set_x, test_set_x.
train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = lr_utils.load_dataset()


# Demonstrates the data:
# ----------------------
pic_index = 100

plt.imshow(train_set_x_orig[pic_index])
plt.show()
y_label = np.squeeze(train_set_y)[pic_index]
# Remove single-dimensional entries from the shape of an array.

print('y = ', train_set_y[:, pic_index], ', it\'s a', classes[y_label], 'picture.')

# Demonstrate the statistics of training examples:
# ---------------------------
num_of_training_data = len(train_set_x_orig) 
num_of_test_data = len(test_set_x_orig)
num_of_pix_of_img = len(train_set_x_orig[1])

print ("Number of training examples: m_train = " + str(num_of_training_data))
print ("Number of testing examples: m_test = " + str(num_of_test_data))
print ("Height/Width of each image: num_px = " + str(num_of_pix_of_img))
print ("Each image is of size: (" + str(num_of_pix_of_img) + ", " + str(num_of_pix_of_img) + ", 3)")
print ("train_set_x shape: " + str(train_set_x_orig.shape))
print ("train_set_y shape: " + str(train_set_y.shape))
print ("test_set_x shape: " + str(test_set_x_orig.shape))
print ("test_set_y shape: " + str(test_set_y.shape))

# Concatenate an image to a single vector
# ---------------------------------------

train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T

# Normalization:
train_set_x = train_set_x_flatten / 255
test_set_x = test_set_x_flatten / 255

def forward(w, b, X, activation_func):

    assert w.T.shape[-1] == X.shape[0]

    Z = np.dot(w.T, X) + b
    A = activation_func(Z)

    return A

def backward(w, b, X, Y, A):
    # dim:
    m = X.shape[1]
    
    cost = (-1 / m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))

    dw = (1 / m) * np.dot(X, (A-Y).T)
    db = (1 / m) * np.sum(A - Y)

    cost = np.squeeze(cost)

    grads = {"dw": dw, "db": db}

    return grads, cost