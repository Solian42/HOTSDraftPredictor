#!/bin/bash
#
# a shell script to automate testing. Makes batch testing simpler.
#
# written by Eric Bridgeford
# #ShellFTW
#
# Usage:
# ./test.sh /path/to/your/code/
#
# If you have any comments or suggestions, send me a message or
# make a PR

# add to this array as we add more algorithms for the class


algorithm=(neural_network logistic_regression knn svm)
#your possible datasetssets
options=(hl_data_hero_only_midmmr hl_data_detailed_highmmr hl_data_hero_only_highmmr hl_data_heroless_highmmr pro_data masters_data masters_data_extra masters_data_heroless hl_data_hero_only hl_data_detailed)

for opt in "${options[@]}"; do
    for algo in "${algorithm[@]}"; do
        # fun little python trick
        start=$(python -c'import time; print(str(time.time()))') # get the time

        # capture stderr in a vara
        trainout=$(python ${1}SciKitHarness.py --mode train --algorithm $algo --model-file datasets/${opt}.${algo}.model --data datasets/${opt}.train 2>&1)

        # capture stderr in a vara
        testout=$(python ${1}SciKitHarness.py --mode test --model-file datasets/${opt}.${algo}.model --data datasets/${opt}.dev --predictions-file datasets/${opt}.dev.predictions 2>&1)
        duration=$(python -c'import time; print(str(time.time() - float('$start')))')

        # make sure we didn't get any errors
        if [[ $trainout == *"Error"* ]] || [[ $testout == *"Error"* ]]; then
            echo "Your code doesn't work for algorithm $algo :("
            if [[ $trainout == *"Error"* ]]; then
                echo "$trainout"
            else
                echo "$testout"
            fi
        else
            acc="$(python compute_accuracy.py datasets/${opt}.dev datasets/${opt}.dev.predictions)"

            echo "${opt} | $algo | $acc | $duration (s)"
        fi
    done
done





