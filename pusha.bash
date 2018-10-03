#!/bin/bash

today=$(date +%Y-%m-%d)

git add -A .
git commit -m "Release: $today"
git push --all

