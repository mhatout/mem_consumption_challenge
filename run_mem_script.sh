#!/bin/bash
touch answers.txt
while IFS= read -r line; do
    echo $line | python task.py >> answers.txt
done < numbers.txt