import csv
import numpy as np
import keras as kr

iris = list(csv.reader(open('iris.csv')))[1:]

inputs  = np.array(iris)[:,:4].astype(np.float)

outputs = np.array(iris)[:,4]

outputs_vals, outputs_ints = np.unique(outputs, return_inverse=True)

outputs_cats = kr.utils.to_categorical(outputs_ints)

inds = np.random.permutation(len(inputs))
train_inds, test_inds = np.array_split(inds, 2)
inputs_train, outputs_train = inputs[train_inds], outputs_cats[train_inds]
inputs_test,  outputs_test  = inputs[test_inds],  outputs_cats[test_inds]


model = kr.models.Sequential()

model.add(kr.layers.Dense(16, input_shape=(4,)))
model.add(kr.layers.Activation("sigmoid"))
model.add(kr.layers.Dense(3))
model.add(kr.layers.Activation("softmax"))

model.summary()