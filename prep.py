# -*- coding: utf-8 -*-
# Import libraries
import chainer
import pickle

# Load the MNIST dataset
train, test = chainer.datasets.get_mnist() # handwritten character
mnist_train = open('./mnist_train.pickle', mode='wb')
mnist_test  = open('./mnist_test.pickle',  mode='wb')
pickle.dump(train, mnist_train)
pickle.dump(test,  mnist_test)
mnist_train.close()
mnist_test.close()


train, test  = chainer.datasets.get_fashion_mnist() # fashion items
fmnist_train = open('./fashion_mnist_train.pickle', 'wb')
fmnist_test  = open('./fashion_mnist_test.pickle',  'wb')
pickle.dump(train, fmnist_train)
pickle.dump(test,  fmnist_test)
fmnist_train.close()
fmnist_test.close()
