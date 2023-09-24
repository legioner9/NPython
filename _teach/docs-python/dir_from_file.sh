#!/bin/bash

cd /home/st/REPOBARE/_repo/NPython/_teach/docs-python || plt_exit "fail: cd /home/st/REPOBARE/_repo/NPython/_teach/docs-python"

for item in *.pdf; do

    n_dir="$(prs_f -n ${item})"
    mkdir -v "${n_dir}"
    mv -v "${item}" "${n_dir}"

done
