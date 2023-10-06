#!/bin/bash

#. "${HOME}/.bashrc"
fntmp_25a123820c() {
    local filename=${PATH_CURR_REPO}/NPython/Pala/flask/selfedu/flask/v_6/.d/.sh/_cr_app_py.sh

    local ARGS=($@)
    if [ "${ARGS[0]}" == "-h" ]; then
        echo -e "${BLUE} 
help from $filename :
1)
${NORMAL}" #sistem info mesage
        return 0
    fi
    NARGS=$#
    local verbose=0
    [[ " ${ARGS[*]} " =~ " -verbose " ]] || verbose=1
    [[ 1 -eq ${verbose} ]] || echo -e "${HLIGHT}---$filename $* ---${NORMAL}" #started functions
    local idir=$(pwd)
    local rdir="$(prs_f -d $filename)"
    local gname="$(prs_f -n $filename)" # name without .ext
    #{header}

    #----------------------------------------------------------------------
    #-------------------------------------
    #-------------------------------

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

    #{body}
    #-------------------------------
    #-------------------------------------
    #----------------------------------------------------------------------

    cd "$idir"

    unset filename
}

fntmp_25a123820c "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8"

unset fntmp_25a123820c
