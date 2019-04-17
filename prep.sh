#!/bin/sh

datadir=$1

if [ ! -e $datadir/train ]; then
    mkdir $datadir/train
fi
if [ ! -e $datadir/eval ]; then
    mkdir $datadir/eval
if

echo 'Download MNIST dataset'
date
if [[ ! -e $datadir/train/mnist_train.pickle || ! -e $datadir/eval/mnist_test.pickle || ! -e $datadir/train/fashion_mnist_train.pickle || ! -e $datadir/eval/fashion_mnist_test.pickle ]]; then
    echo "start download data"
    python ./prep.py #download MNIST dataset
    mv mnist_train.pickle $datadir/train/
    mv mnist_test.pickle $datadir/eval/
    mv fashion_mnist_train.pickle $datadir/train/
    mv fashion_mnist_test.pickle $datadir/eval/
else
    echo "data is already prepared, skip"
fi
touch $datadir/done
