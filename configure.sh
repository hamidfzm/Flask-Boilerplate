#!/usr/bin/env bash
# TODO choose extensions
# TODO choose blueprints
# TODO choose form

checkApp(){
    if ! which $1 > /dev/null; then
        echo "$1 not found."
        exit
    fi
}

checkApp pipenv

if [ ! -f Pipfile ]; then
    echo "Pipfile not found."
    read -p "Do you want to setup Pipenv? [y|n]: " -n 2 -r
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo
        read -p "Type python app location: "
        pipenv --python $REPLY
        if [ $? -ne 0 ]; then
            rm -rf Pipfile
            exit
        fi

        pipenv install flask

    else
        exit
    fi

fi
