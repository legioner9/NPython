#!/bin/bash

#. "$HOME/.bashrc"

filename="/home/st/REPOBARE/_repo/NPython/sfu/tasks_II/v_5/.d/.sh/_cr_app_py.sh"

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

sh_cr_app_py() {
    echo -e "${HLIGHT}--- sh_cr_app_py ---${NORMAL}" #start files

    local rdir="/home/st/REPOBARE/_repo/NPython/sfu/tasks_II/v_5/.d/.sh"

    local app_dir="${rdir}"/../..
    local tml_dir="${rdir}"/../.tml
    local res_dir="${rdir}"/../.res
    local curr_dir="${rdir}"/../.curr
    local lst2_dir="${rdir}"/../.lst2

    local app_file="${app_dir}"/app.py
    local app_tml="${tml_dir}/app.tml"

    local anc_head="${tml_dir}/anc_head.tml"
    local insert_decfn="${tml_dir}/insert_decfn.tml"
    local decfn="${tml_dir}/decfn.tml"

    local str

   "${_ehh}" rm "${app_file}"
   "${_ehh}" cp "${app_tml}" "${app_file}"

    "${_cr_f_}" \
            "${app_file}" \
            --fi0 "${anc_head}" --fr0 "{anc_head}"

    for str in $(f2e ${lst2_dir}/routaddr_namefn.lst2); do

        local str_parr=()

        "${_s3parr_}" --_str "${str}" --_del ":" --_parr str_parr
        "${_parr3e_}" str_parr

       "${_ehh}" rm "${insert_decfn}"
       "${_ehh}" cp "${decfn}" "${insert_decfn}"

        file_return=""${curr_dir}/${str_parr[1]}".curr"

        "${_cr_f_}" \
            "${insert_decfn}" \
            --vi0 "${str_parr[0]}" --vr0 "{str_parr_0}" \
            --vi1 "${str_parr[1]}" --vr1 "{str_parr_1}" \
            --fi0 "${file_return}" --fr0 "{file_return}"

        "${_ehh}" cat "${insert_decfn}"

        "${_cr_f_}" \
            "${app_file}" \
            --fi1 "${insert_decfn}" --fr1 "{insert_decfn}"

    done

    sed -i -e 's/{}/ /g' "${app_file}"
}

sh_cr_app_py

#{body}
#-------------------------------
#-------------------------------------
#----------------------------------------------------------------------

cd "$idir"

unset filename
