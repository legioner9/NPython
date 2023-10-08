#!/bin/bash

#. "${HOME}/.bashrc"
fntmp_f76e523211() {

    local filename=${PATH_CURR_REPO}/NPython/Pala/flask/selfedu/flask/v_7/via.sh

    local ARGS=($@)
    if [ "${ARGS[0]}" == "-h" ]; then
        echo -e "${BLUE} 
help from $filename :
1) menu flow for app.py - start, rebuild, check and mute routs
2) first using url_for
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
    echo -e "${BLUE}--- exec ${FNN} (num_menu) ---${NORMAL}" #started functions
    local arr=()
    local res=()

    #{arr_res}

    arr+=("start app.py")
    res+=(". ${rdir}/.d/.sh/_start_check.sh -s")

    arr+=("deletion + creation app.py")
    res+=(". ${rdir}/.d/.sh/_cr_app_py.sh")

    # arr+=("deletion + creation + start app.py")
    # res+=(". ${PATH_CURR_REPO}/NPython/Pala/flask/selfedu/flask/v_7/.d/.sh/_cr_app_py.sh ;\
    # . ${PATH_CURR_REPO}/NPython/Pala/flask/selfedu/flask/v_7/.d/.sh/_start_check.sh -s")

    arr+=("check pages server")
    res+=(". ${rdir}/.d/.sh/_start_check.sh -c")

    arr+=("correct routaddr_namefn.lst2")
    res+=("edit_ ${rdir}/.d/.lst2/routaddr_namefn.lst2")

    arr+=("correct .d/.ecce/ligitur.man")
    res+=("edit_ ${rdir}/.d/.ecce/legitur.man")
    # REPOBARE/_repo/NPython/Pala/flask/selfedu/flask/v_7/.d/.ecce/legitur.man

    # arr+=("aaaaaaaaa")
    # res+=("bbbbbbbbb")
    # arr+=("aaaaaaaaa")
    # res+=("bbbbbbbbb")
    # arr+=("aaaaaaaaa")
    # res+=("bbbbbbbbb")
    # arr+=("aaaaaaaaa")
    # res+=("bbbbbbbbb")
    # arr+=("aaaaaaaaa")
    # res+=("bbbbbbbbb")
    # arr+=("aaaaaaaaa")
    # res+=("bbbbbbbbb")
    # arr+=("aaaaaaaaa")
    # res+=("bbbbbbbbb")

    if [ $(num_01 $1) -eq 1 ] && [ $1 -le ${#arr[@]} ]; then
        num_res=$(($1 - 1))
        ${res[${num_res}]}
        return 0
    fi
    PS3="eligendi actiones: "
    select item in "${arr[@]}"; do
        for ((i = 0; i < 1000; i++)); do
            if [[ ${item} == ${arr[$i]} ]]; then
                ${res[$i]}
                ${FNN} $@
            fi
            if [[ ${item} == ${arr[0]} ]]; then
                ${res[$i]}
            fi
        done
    done
    #{body}
    #-------------------------------
    #-------------------------------------
    #----------------------------------------------------------------------

    cd "$idir"

    unset filename
}

fntmp_f76e523211 "$1" $2 $3 $4 $5 $6 $7 $8

unset fntmp_f76e523211
