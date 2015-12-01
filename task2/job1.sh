#!/bin/sh

echo "hdfs dfs -rm -r /user/\$USER/data/Assignment2/task2/output/ ;
hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -D stream.num.map.output.key.fields=2 \
 -D num.key.fields.for.partition=1 \
 -D mapreduce.partition.keypartitioner.options=\"-n1,1\" \
 -D mapreduce.partition.keycomparator.options=\"-n1,2\" \
 -input /user/\$USER/data/Assignment2/task1/output/job2 \
 -output /user/\$USER/data/Assignment2/task2/output/ \
 -mapper mapper1.py \
 -reducer reducer1.py \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
 -file Documents/EXC/Assignment2/task2/terms.txt \
 -file Documents/EXC/Assignment2/task2/input/mapper1.py \
 -file Documents/EXC/Assignment2/task2/input/reducer1.py \
 -jobconf mapred.job.name=\"Sam's tf-idf\" ;"