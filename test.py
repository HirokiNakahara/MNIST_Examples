# Import libraries
import chainer
import chainer.functions as F
import chainer.links as L
from chainer import training
from chainer.training import extensions
from chainer.dataset import concat_examples
from chainer.backends.cuda import to_cpu
import numpy as np
import matplotlib.pyplot as plt
from chainer import Variable
import pickle
import os

home_dir = os.path.expanduser('~')

# Check environment
print('GPU availability:', chainer.cuda.available)
print('cuDNN availablility:', chainer.cuda.cudnn_enabled)
chainer.print_runtime_info()

"""ニューラルネットワークの定義"""
# Define Binary DNN (3-layers), note that, we use a mixed-precision (Binary + Float32) neural network
# To preserve a recognition accuracy. If you want learn more, see my FPGA'18 paper!
class MNIST(chainer.Chain):

    def __init__(self,n_mid_units=100,n_out=10):
        super(MNIST, self).__init__()
        with self.init_scope():
            # the size of the inputs to each layer will be inferred
            self.l1 = L.Linear(784, n_mid_units)
            self.l2 = L.Linear(n_mid_units, n_mid_units)
            self.l3 = L.Linear(n_mid_units, n_out)

    def __call__(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        return self.l3(h2)

# Setup parameters
args_gpu=0 # 0: GPU (strongly recommendded), -1: CPU
args_unit=100 # The number of neurons in hidden layers
#args_batchsize=100

# Printout parameters
print('GPU: {}'.format(args_gpu))
print('# unit: {}'.format(args_unit))
print('')

model = MNIST()
if args_gpu >= 0:
    # Make a specified GPU current
    chainer.backends.cuda.get_device_from_id(args_gpu).use()
    model.to_gpu()  # Copy the model to the GPU
chainer.serializers.load_npz(home_dir + '/MNIST/mnist.model',model)

"""学習データであるMNISTデータセット(またはFashion MNIST)の読み込み。"""
# Load the MNIST dataset
# handwritten character
mnist_test  = open('./mnist_test.pickle',  'rb')
# fashion items
#mnist_test  = open('./fashion_mnist_test.pickle',  'rb')

test  = pickle.load(mnist_test)
mnist_test.close()

def show_examples(model, test, device):
    plt.figure(figsize=(12,50))
#    if device < 0:
#        print("to cpu")
#        model.to_cpu()
    model.to_cpu()
    for i in range(45, 55):
        data, label = test[i]  # test data, label
        x = Variable(np.asarray([data]))
        t = Variable(np.asarray([label]))  # labels
        y = model(x)
        prediction = y.data.argmax(axis=1)
        example = (data * 255).astype(np.int32).reshape(28, 28)
        plt.subplot(20, 5, i - 44)
        plt.imshow(example, cmap='gray')
        plt.title("No.{0}\nAnswer:{1}\nPredict:{2}".format(
            i,
            label,
            prediction[0]
        ))
        plt.axis("off")
    plt.tight_layout()

show_examples(model, test, args_gpu)
plt.savefig(home_dir + '/MNIST/show_example.png')
