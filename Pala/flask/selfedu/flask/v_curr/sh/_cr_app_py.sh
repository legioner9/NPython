#!/bin/bash

#. "$HOME/.bashrc"

filename="/home/st/REPOBARE/_repo/NPython/Pala/flask/selfedu/flask/v_curr/sh/_cr_app_py.sh"

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
f0() {
    local app_dir="${rdir}"/..
    local str

    for str in $(f2e routaddr_namefn.lst2); do
        local str_parr=()

        s3parr_ --_str "${str}" --_del ":" --_parr str_parr
        parr3e_ str_parr

        rm insert_decfn.tml
        cp decfn.tml insert_decfn.tml
        cr_f_ insert_decfn.tml --vi0 "${str_parr[0]}" --vr0 "{str_parr_0}" \
            --vi1 "${str_parr[1]}" --vr1 "{str_parr_1}" \
            --fi0 "${str_parr[1]}".curr --fr0 "{file_return}"

        sed -i -e 's/|/ /g' insert_decfn.tml

        ehh cat insert_decfn.tml
    done
}

f0

#{body}
#-------------------------------
#-------------------------------------
#----------------------------------------------------------------------

cd "$idir"

unset filename
