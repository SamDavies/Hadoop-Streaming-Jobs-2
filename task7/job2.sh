#!/bin/sh

echo "hdfs dfs -rm -r /user/\$USER/data/Assignment2/task7/output/job2/ ;
hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
 -D mapred.text.key.comparator.options=-nr \
 -input /user/\$USER/data/Assignment2/task7/output/job1/ \
 -output /user/\$USER/data/Assignment2/task7/output/job2/ \
 -mapper cat \
 -reducer reducer2.py \
 -file Documents/EXC/Assignment2/task7/input/reducer2.py \
 -jobconf mapred.job.name=\"Sam's stack overflow most answered part 2\" ;"