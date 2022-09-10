#!/bin/bash


#This directory
DIR="$PWD/solutions"

if [[ -z "${PYTHONPATH}" ]]; then
	export PYTHONPATH=$DIR
else
	if [[ $PYTHONPATH == *$DIR* ]]; then
		export PYTHONPATH = "$PYTHONPATH:$DIR"
	fi
fi

echo "PYTHONPATH variable is:"
echo $PYTHONPATH
