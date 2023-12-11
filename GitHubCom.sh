#!/bin/bash

if [ "$#" -ne 3 ]; then
	echo "Usage: GitHubCom.sh <File> <Message> <Command>"
	exit 1
fi
git $3 $1 && git commit -m "$2"
git push
