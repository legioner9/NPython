#!/bin/bash

#. "$HOME/.bashrc"

filename="/home/st/REPOBARE/_repo/NPython/Pala/flask/selfedu/flask/v_curr/start_check.sh"

ARGS=($@)
NARGS=$#
verbose=0
[[ " ${ARGS[*]} " =~ " -verbose " ]] || verbose=1
[[ 1 -eq ${verbose} ]] || echo -e "${HLIGHT}---$filename $* ---${NORMAL}" #started functions
idir=$(pwd)
rdir="$(prs_f -d $filename)"
gname="$(prs_f -n $filename)" # name without .ext
wrp_fifs1_ cd "$(prs_f -d $filename)" -d1
g_args=($(garg2e_ "${ARGS[@]}"))
[[ 1 -eq ${verbose} ]] || echo -e "${GREEN}\${g_args[@]}: ${g_args[*]}${NORMAL}" #print variable
for strex in $(garg2e_ "${ARGS[@]}"); do
    [[ 1 -eq ${verbose} ]] || echo "local $strex"
    eval $strex
done
_() {
    echo "empty _deb in $filename"
    # . $filename" arg1 arg2
}
if [ "_deb" == "$1" ]; then
    _
    return 0
fi
#{header}

#----------------------------------------------------------------------
#-------------------------------------
#-------------------------------
A1="$1"
echo -e "${GREEN}\$A1 = $A1${NORMAL}" #print variable
h() {
    echo -e "arg1:
-s start app
-c check domain 
"
}

fh() {
    plt_info "arg1 NOT:
-s start app,
-c check domain
"
}

h

if [ "$A1" == "-s" ]; then

    echo -e "${HLIGHT}--- start app mode ---${NORMAL}" #start files
    ehh python3 "${rdir}"/app.py
    return 0

fi

if [ "$A1" == "-c" ]; then

    echo -e "${HLIGHT}--- check mode ---${NORMAL}"                                    #start files
    [ "$(curl http://127.0.0.1:5000)" == "index page" ] || plt_info "index page fail" #exit 1 "index page fail"
    [ "$(curl http://127.0.0.1:5000/about)" == "<h1>About site</h1>" ] || plt_info "About page fail"
    return 0

fi

fh

#{body}
#-------------------------------
#-------------------------------------
#----------------------------------------------------------------------

cd "$idir"

unset filename
