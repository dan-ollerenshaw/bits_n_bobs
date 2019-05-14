#!/bin/sh

# Use this to delete HDFS files in a particular
# directory that contain a particular string

FPATH=$1
STRING=$2
for file in `hdfs dfs -ls $FPATH | grep $STRING | awk '{print $8}'`
do
hdfs dfs -rm -r $file
done