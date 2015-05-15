#!/bin/bash
merp() {
	ANSWER=$(python queryprocess.py $*)
	echo $*
	echo $ANSWER
	./tts.sh $ANSWER
	}
merp $*
