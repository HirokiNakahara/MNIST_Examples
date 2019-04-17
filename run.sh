#!/bin/sh

datadir=/gs/hs0/tga-egliteracy/data/MNIST_Examples
modeldir=$PWD

########### skipping data download for tsubame using ###############
########### data has been save at /gs/hs0/tga-egliteracy/data/MNIST_Examples ##############

#date
# ./prep.sh $datadir >&prep.log

##################################################################

traindata=$datadir/train
evaldata=$datadir/eval

echo 'Start training'
date
python ./train.py >& train.log

echo 'Evaluation and plot example'
data
python ./eval.py >& eval.log

date
