#!/bin/sh

echo "start"

mkdir -p ~/MNIST
if [ -e ~/MNIST/run.log ] ; then
    echo "log exist, delete"
    rm ~/MNIST/run.log
fi

qsub -g tga-egliteracy -o ~/MNIST/run.log -e ~/MNIST/run.log qsub_run.sh
