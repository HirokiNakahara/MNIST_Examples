#!/bin/sh

datadir=/gs/hs0/tga-egliteracy/data/MNIST_Examples
modeldir=$PWD/model

echo 'start time'
date
echo '-----------------'

########### skipping data download for tsubame using ###############
########### data has been save at /gs/hs0/tga-egliteracy/data/MNIST_Examples ##############

#date
# ./prep.sh $datadir >&prep.log

##################################################################

traindata=$datadir/train1
# traindata=$datadir/train20
# traindata=$datadir/train40
# traindata=$datadir/train60
# traindata=$datadir/train80
# traindata=$datadir/train100
evaldata=$datadir/eval

echo 'Start training'
start_time=`date +%s`
# date
./train.sh $modeldir $traindata  >& train.log
end_time=`date +%s`
time="$((end_time - start_time)) (sec)"
echo $time >& train.time.log

echo 'Evaluation'
# date
./eval.sh $modeldir $evaldata >& eval.log

echo '------------------'
echo 'final end time'
date
