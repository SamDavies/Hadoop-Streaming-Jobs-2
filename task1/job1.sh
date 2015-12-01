#!/bin/sh

echo "hdfs dfs -rm -r /user/\$USER/data/Assignment2/task1/output/job1/ ;
hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -D stream.num.map.output.key.fields=2 \
 -D num.key.fields.for.partition=1 \
 -D mapreduce.partition.keypartitioner.options=\"-k1,1\" \
 -D mapreduce.partition.keycomparator.options=\"-k1,2\" \
 -input /data/assignments/ex2/task1/large/ \
 -output /user/\$USER/data/Assignment2/task1/output/job1 \
 -mapper mapper1.py \
 -reducer reducer1.py \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
 -file Documents/EXC/Assignment2/task1/input/mapper1.py \
 -file Documents/EXC/Assignment2/task1/input/reducer1.py \
 -jobconf mapred.job.name=\"Sam's inverted index part 1\" ;"