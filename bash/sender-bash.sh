#!/bin/bash

while read line; do
    for word in $line; do
        echo "word = '$word'"
    done
done <"data.txt"
