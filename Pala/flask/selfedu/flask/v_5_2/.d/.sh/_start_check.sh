#!/bin/bash

#. "${HOME}/.bashrc"
fntmp_eeb0732bd8() {
    local filename=${PATH_CURR_REPO}/NPython/sfu/tasks_II/v_5/.d/.sh/_start_check.sh

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
    local ARGS0="${ARGS[0]}"
    local sh_dir=${rdir}
    local app_dir=${rdir}/../..

    fh() {
        echo -e "ARGS0:
    -s: start app
    -c: check domain after start in new shall
"
    }

    ferr() {
        plt_info "ARGS0 NOT: -s start app, -c check domain"
    }

    fh

    if [ "$ARGS0" == "-s" ]; then

        echo -e "${HLIGHT}--- start app mode ---${NORMAL}" #start files
        ${_ehh} python3 "${app_dir}"/app.py
        return 0

    fi

    if [ "$ARGS0" == "-c" ]; then
        echo -e "${HLIGHT}--- check mode ---${NORMAL}"

        local app_dir="${rdir}"/../..
        local tml_dir="${rdir}"/../.tml
        local res_dir="${rdir}"/../.res
        local pre_dir="${rdir}"/../.pre
        local curr_dir="${rdir}"/../.curr
        local lst2_dir="${rdir}"/../.lst2

        local app_file="${app_dir}"/app.py
        local app_tml="${tml_dir}/app.tml"

        local anc_head="${tml_dir}/anc_head.tml"
        local insert_decfn="${tml_dir}/insert_decfn.tml"
        local decfn="${tml_dir}/decfn.tml"

        local str

        for str in $(f2e ${lst2_dir}/routaddr_namefn.lst2); do

            local str_parr=()

            "${_ehh}" "${_s3parr_}" --_str "${str}" --_del ":" --_parr str_parr
            "${_ehh}" "${_parr3e_}" str_parr

            local str_parr_0=${str_parr[0]}
            local str_parr_1=${str_parr[1]}

            local file_pre="${pre_dir}/${str_parr_1}.pre"
            local file_res="${res_dir}/${str_parr_1}.res"

            : >"${file_res}"

            "${_ehh}" curl -o "${file_res}" http://127.0.0.1:5000"${str_parr_0}"

            if ! diff -q "${file_res}" "${file_pre}" >/dev/null; then
                plt_info "fail ${str_parr_1}.html"
            else
                echo -e "${GREEN}--- OK ${str_parr_1}.html ---${NORMAL}" #print variable
            fi

        done
        return 0
    fi

    ferr

    #{body}
    #-------------------------------
    #-------------------------------------
    #----------------------------------------------------------------------

    cd "$idir"

    unset filename
}

fntmp_eeb0732bd8 "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8"

unset fntmp_eeb0732bd8
