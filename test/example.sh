#!/bin/bash

INPUT="./input.result.txt"

python ../targetpred.py \
    -i ${INPUT} \
    -o ./out \
    -p example 
