#!/bin/sh

echo "hdfs dfs -rm -r /user/\$USER/data/Assignment2/task7/output/job3/ ;
hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
 -D mapred.text.key.comparator.options=-nr \
 -D mapreduce.job.reduces=1 \
 -input /user/\$USER/data/Assignment2/task7/output/job2/ \
 -output /user/\$USER/data/Assignment2/task7/output/job3/ \
 -mapper cat \
 -reducer reducer3.py \
 -file Documents/EXC/Assignment2/task7/input/reducer3.py \
 -jobconf mapred.job.name=\"Sam's stack overflow most answered part 3\" ;"