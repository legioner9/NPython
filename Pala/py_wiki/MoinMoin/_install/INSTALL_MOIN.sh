#!/bin/bash

# PATH_MONI_APP_DIR=${HOME}/MoniMoniApp # in standart replace: /usr/local to ${MONI_APP_DIR}

cd ${HOME}/REPOBARE/_repo/NPython/Pala/py_wiki/MoinMoin/moin-${VERSION_MOIN_APP} || plt_exit "cd fail"

read -p "delit? ${PATH_MONI_APP_DIR} continue ENTER or cancel ^C"

rm -rf ${PATH_MONI_APP_DIR}

sudo python"${VERSION_PYTHON_FOR_MOIN_APP}" setup.py install --prefix="${PATH_MONI_APP_DIR}"

cd "${PATH_MONI_APP_DIR}"/share/moin || plt_exit "cd fail"

cp server/moin.wsgi .
