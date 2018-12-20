import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


print("Loading data...\n")
train=np.loadtxt('train_data.txt')
test = np.loadtxt('test_data.txt')

x_train = train[:,0:11]
y_train = train[:,-1]
x_test = test[:,0:11]
y_test = test[:,-1]

print('Traing model...')
# Train model here
clf_rf = RandomForestClassifier(n_estimators = 500)
clf_rf.fit(x_train,y_train)

# Model error analysis here
print('Accuracy: Test set on Random forest: ', clf_rf.score(x_test, y_test))
target_names = ['3', '4', '5', '6', '7', '8']
print()
print(classification_report(y_test, clf_rf.predict(x_test), target_names=target_names))


# Predict given test input
test_input = np.loadtxt('input_test.txt')
test_input = preprocessing.scale(test_input)
#print(clf_rf.predict(test_input))
np.savetxt('result.txt', clf_rf.predict(test_input), delimiter = ' ', newline = '\n', fmt = '%d')




