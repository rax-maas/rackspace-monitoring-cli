#!/bin/sh
# optcomplete harness for bash shell. You then need to tell 
# bash to invoke this shell function with a command like 
# this::
#
#   complete -F _optcomplete <program>
#

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

_optcomplete()
{
    COMPREPLY=( $( \
    COMP_LINE=$COMP_LINE  COMP_POINT=$COMP_POINT \
    COMP_WORDS="${COMP_WORDS[*]}"  COMP_CWORD=$COMP_CWORD \
    OPTPARSE_AUTO_COMPLETE=1 $1 ) )
}

source ${DIR}/completions.sh
