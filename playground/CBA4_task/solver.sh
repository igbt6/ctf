#!/bin/bash
file="passwords"
while read -r line
do
    echo "$line"
    7z x 4.7z -y -p$line
done < "$file"