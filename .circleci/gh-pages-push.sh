#!/bin/bash -eux

if [[ -z $CIRCLE_PULL_REQUEST ]] ; then
    git clone --single-branch -b gh-pages git@github.com:heliophysicsPy/gallery.git gh-pages
    cp -r _build/html/* gh-pages
    cd gh-pages
    git add .
    git status
    git -c user.name='circle' -c user.email='circle' commit -m "Upadate the build docs"
    git status
    git push -q origin gh-pages
    echo "Not a pull request: pushing RST files to rst branch."
else
    echo $CIRCLE_PULL_REQUEST
    echo "This is a pull request: not pushing RST files."
fi
