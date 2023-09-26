#!/bin/bash

# PATH_MONI_APP_DIR=${HOME}/MoniMoniApp # in standart replace: /usr/local to ${MONI_APP_DIR}

#? install MoinMoin

echo -e "${GREEN}\$VERSION_MOIN_APP = ${VERSION_MOIN_APP}${NORMAL}"                       #print variable
echo -e "${GREEN}\$PATH_MONI_APP_DIR = ${PATH_MONI_APP_DIR}${NORMAL}"                     #print variable
echo -e "${GREEN}\$VERSION_PYTHON_FOR_MOIN_APP = ${VERSION_PYTHON_FOR_MOIN_APP}${NORMAL}" #print variable
echo -e "${GREEN}\$PATH_MONI__ISSUE_DIR = ${PATH_MONI__ISSUE_DIR}${NORMAL}"               #print variable

plt_pause "that current env for you project?"

if plt_is_ques "install? :: MoinMoin in ${PATH_MONI_APP_DIR}"; then

    plt_vae cd "${PATH_MONI__ISSUE_DIR}"

    plt_ques_exec "wget http://static.moinmo.in/files/moin-${VERSION_MOIN_APP}.tar.gz"

    plt_ques_exec "tar zxvf moin-${VERSION_MOIN_APP}.tar.gz"

    plt_vae "cd ${PATH_MONI__ISSUE_DIR}/moin-${VERSION_MOIN_APP}"

    plt_ques_exec "rm -rf ${PATH_MONI_APP_DIR}"

    plt_ques_exec "sudo python${VERSION_PYTHON_FOR_MOIN_APP}" setup.py install --prefix="${PATH_MONI_APP_DIR}"

fi

#? setting MoinMoin

if plt_is_ques "setting? :: MoinMoin"; then

    plt_vae "cd ${PATH_MONI_APP_DIR}/share/moin"

    plt_ques_exec cp server/moin.wsgi .

    echo -e "sudo vi moin.wsgi
    После строки import sys, os вставьте следующий код:
 
        sys.path.insert(0, '/usr/local/lib/python2.7/dist-packages/')
        sys.path.insert(0, '/usr/local/share/moin/')

    Сохраните и закройте файл. Эти строки указывают расположение кода MoinMoin и конфигурационных файлов вики.

    sudo vi uwsgi.ini

    Добавьте в этот файл следующие строки:

        [uwsgi] uid = www-data
        gid = www-data
        socket = /usr/local/share/moin/moin.sock
        chmod-socket = 660
        logto = /var/log/uwsgi/uwsgi.log
        chdir = /usr/local/share/moin/
        wsgi-file = moin.wsgi
        master
        workers = 3
        max-requests = 200
        harakiri = 30
        die-on-term
    "

fi

#? setting nginx for MoinMoin

if plt_is_ques "setting? :: nginx for MoinMoin"; then

    echo -e "sudo vi /etc/nginx/sites-available.d/moin

    server {
    server_name localhost_moin;
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;
    location / {
    include uwsgi_params;
    uwsgi_pass unix://${PATH_MONI_APP_DIR}/share/moin/moin.sock;
    uwsgi_modifier1 30;
    }
    }
    
    cd /etc/nginx/sites-enabled
    sudo ln -s ../sites-available/moin .

    sudo service nginx restart

    переход: http://localhost_moin
    "
    plt_pause "do this instruction?"
fi
