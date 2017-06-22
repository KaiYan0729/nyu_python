#!/usr/bin/env bash

export RUN_USER="ubuntu"
export RUNUSER_PROG="/$bin/runuser"
#export COMMAND="echo $USER"
export COMMAND=$(cat <<-'HERE1a'
	echo $USER
	echo $HOME
	cd /tmp
	echo $PWD
HERE1La
)

sudo ${RUNUSER_PROG} -l ${RUN_USER} -c "${COMMAND}"

