#!/bin/bash

cd ${HOME}/REPOBARE/_repo/NPython/Pala/py_wiki/MoinMoin/moin-1.9.11 || plt_exit "cd fail"

rm -ri ${HOME}/MoniMoniApp

sudo python2.7 setup.py install --prefix=${HOME}/MoniMoniApp
