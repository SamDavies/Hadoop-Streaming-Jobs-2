#!/bin/sh

echo "hdfs dfs -rm -r /user/\$USER/data/Assignment2/task6/output/job1/ ;
hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
 -D mapred.text.key.comparator.options=-nr \
 -input /data/assignments/ex2/task3/stackLarge.txt \
 -output /user/\$USER/data/Assignment2/task6/output/job1/ \
 -mapper mapper1.py \
 -reducer reducer1.py \
 -file Documents/EXC/Assignment2/task6/input/mapper1.py \
 -file Documents/EXC/Assignment2/task6/input/reducer1.py \
 -jobconf mapred.job.name=\"Sam's stack overflow most viewed part 1\" ;"