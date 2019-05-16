#!/bin/sh

modeldir=$1
if [ ! -e $modeldir ]; then
    mkdir $modeldir
fi
if [ -e $modeldir/mnist.model ]; then
    echo 'model is already trained, skip'
else
    python -W ignore train.py --modeldir $modeldir --datadir $2
fi
touch $modeldir/done
