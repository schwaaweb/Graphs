#!/bin/bash

git remote
git remote add upstream https://github.com/LambdaSchool/Graphs
git remote
git fetch upstream
pwd
git merge upstream/master
git status
git add .
git status
git commit -am "updated the upstream branch of the Graphs repository"
git status
git push
