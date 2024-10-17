#!/bin/bash


first=$( echo $1 | grep -Eo '[+-]?[0-9]+([.][0-9]+)' )
second=$( echo $2 | grep -Eo '[+-]?[0-9]+([.][0-9]+)' )

echo "$first"
echo "$second"

if (( $(echo "$first > $second" |bc -l) )); then
    echo "first larger than second"
fi
