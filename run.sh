#!/bin/sh

########### skipping data download for tsubame using ###############
########### data has been save at /gs/hs0/tga-egliteracy/data/MNIST_Examples ##############

#echo 'Download MNIST dataset'
#date
#if [[ ! -e mnist_train.pickle || ! -e mnist_test.pickle || ! -e fashion_mnist_train.pickle || ! -e fashion_mnist_test.pickle ]]; then
#    echo "start download data"
#    python ./prep.py >& prep.log #download MNIST dataset
#else
#    echo "data exist, skip downloading"
#fi

##################################################################

echo 'Start training'
date
python ./train.py >& train.log

echo 'Evaluation and plot example'
data
python ./eval.py >& eval.log

date
