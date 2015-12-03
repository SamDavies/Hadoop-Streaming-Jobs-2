#!/bin/sh

echo "hdfs dfs -rm -r /user/\$USER/data/Assignment2/task7/output/job1/ ;
hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -D stream.num.map.output.key.fields=2 \
 -D num.key.fields.for.partition=1 \
 -D mapreduce.partition.keypartitioner.options=\"-k1,1\" \
 -D mapreduce.partition.keycomparator.options=\"-k1,2\" \
 -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
 -D mapred.text.key.comparator.options=-nr \
 -input /data/assignments/ex2/task3/stackLarge.txt \
 -output /user/\$USER/data/Assignment2/task7/output/job1/ \
 -mapper mapper1.py \
 -reducer reducer1.py \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
 -file Documents/EXC/Assignment2/task7/input/mapper1.py \
 -file Documents/EXC/Assignment2/task7/input/reducer1.py \
 -jobconf mapred.job.name=\"Sam's stack overflow most answered part 1\" ;"