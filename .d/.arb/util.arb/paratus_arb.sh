#!/bin/bash

#! inner procedure IFS for ${PLT_PATH}/.d/.sal.ax/fol_/fol_.sal
#! local var {item_ram_} {item_tag_}
#! {arb_} full path to arb dir with .ram files 

: >"${arb_}"/all_ramus_name.lst
for item_ram_ in $("${_dd2e}" "${arb_}"); do
    echo "$(prs_f -n "${item_ram_}")" >>"${arb_}"/all_ramus_name.lst
done

: >${arb_}/all_unique_tags.lst
for item_tag_1 in $(${_f2e} "${arb_}"/all_ramus_name.lst); do

    for item_tag_2 in $(${_f2e} ${arb_}/${item_tag_1}.ram/tags.fol); do
        if ! grep -w ${item_tag_2} ${arb_}/all_unique_tags.lst &>/dev/null; then
            echo ${item_tag_2} >>${arb_}/all_unique_tags.lst
        fi
    done

done

${_sort_tags_s} ${arb_}/all_unique_tags.lst
${_sort_tags_s} ${arb_}/all_ramus_name.lst