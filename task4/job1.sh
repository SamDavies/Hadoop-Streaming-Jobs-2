#!/bin/sh

echo "hdfs dfs -rm -r /user/\$USER/data/Assignment2/task4/output/job1/ ;
hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -input /data/assignments/ex2/task2/logsLarge.txt \
 -output /user/\$USER/data/Assignment2/task4/output/job1/ \
 -mapper mapper1.py \
 -reducer reducer1.py \
 -file Documents/EXC/Assignment2/task4/input/mapper1.py \
 -file Documents/EXC/Assignment2/task4/input/reducer1.py \
 -jobconf mapred.job.name=\"Sam's top 10 404s part 1\" ;"