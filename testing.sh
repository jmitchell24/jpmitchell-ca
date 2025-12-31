#! /usr/bin/bash 

xdg-open "http://127.0.0.1:8080" > /dev/null 2>&1 &

zola serve --drafts --interface 0.0.0.0 --port 8080