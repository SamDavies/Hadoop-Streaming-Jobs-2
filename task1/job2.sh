#!/bin/sh

echo "hdfs dfs -rm -r /user/\$USER/data/Assignment2/task1/output/job2/ ;
hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -D mapreduce.job.reduces=1 \
 -input /user/\$USER/data/Assignment2/task1/output/job1 \
 -output /user/\$USER/data/Assignment2/task1/output/job2 \
 -mapper cat \
 -reducer reducer2.py \
 -file Documents/EXC/Assignment2/task1/input/reducer2.py \
 -jobconf mapred.job.name=\"Sam's inverted index part 2\" ;"