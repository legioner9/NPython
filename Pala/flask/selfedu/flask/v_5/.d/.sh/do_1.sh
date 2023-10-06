#!/bin/bash

#. "$HOME/.bashrc"

filename="/home/st/REPOBARE/_repo/NPython/Pala/flask/selfedu/flask/v_5/.d/.sh/do_1.sh"

ARGS=($@)
echo -e "${GREEN}\${ARGS[@]} = ${ARGS[*]}${NORMAL}" #print variable
NARGS=$#
verbose=0
[[ " ${ARGS[*]} " =~ " -verbose " ]] || verbose=1
[[ 1 -eq ${verbose} ]] || echo -e "${HLIGHT}---$filename $* ---${NORMAL}" #started functions
idir=$(pwd)
rdir_="$(prs_f -d $filename)"
gname="$(prs_f -n $filename)" # name without .ext


#{header}

#----------------------------------------------------------------------
#-------------------------------------
#-------------------------------

if [ "${ARGS[0]}" == -"h" ]; then

    echo -e "${BLUE}--- message:

1) create ${rdir_}/../../app.py
2) start ${rdir_}/../../app.py

 ---${NORMAL}" #sistem info mesage
    return 0
fi

echo -e "${HLIGHT}--- . ${rdir_}/_cr_app_py.sh ---${NORMAL}" #start files
. ${rdir_}/_cr_app_py.sh
echo -e "${HLIGHT}--- . ${rdir_}/_start_check.sh ---${NORMAL}" #start files
. ${rdir_}/_start_check.sh -s

#{body}
#-------------------------------
#-------------------------------------
#----------------------------------------------------------------------

cd "$idir"

unset filename
