#!/bin/sh

TASK="$1"

DIR="${PWD}"

scp -rp $DIR/task$TASK/input s1220039@student.ssh.inf.ed.ac.uk:/afs/inf.ed.ac.uk/user/s12/s1220039/Documents/EXC/Assignment2/task$TASK/

# remove the existing output directory
ssh -t -t s1220039@student.ssh.inf.ed.ac.uk << EOL
    rm -r /afs/inf.ed.ac.uk/user/s12/s1220039/Documents/EXC/Assignment2/task$TASK/output/job1
    rm -r /afs/inf.ed.ac.uk/user/s12/s1220039/Documents/EXC/Assignment2/task$TASK/output/job2
    exit
EOL

echo ""
echo "JOB COMMAND 1"
echo "-----------"
. task$TASK/job1.sh
echo ""

echo "JOB COMMAND 2"
echo "-----------"
. task$TASK/job2.sh
echo ""

echo "COPY RESULTS COMMAND"
echo "---------------------"
#echo "hdfs dfs -rm -r /user/\$USER/\${USER}_task_${TASK}.out;"
#echo "hdfs dfs -cp /user/\$USER/data/output /user/\$USER/\${USER}_task_${TASK}.out;"
echo "hdfs dfs -copyToLocal /user/\$USER/data/output/job2 /afs/inf.ed.ac.uk/user/s12/s1220039/Documents/EXC/Assignment2/task$TASK/"
echo ""

echo "LOCAL COPY RESULTS COMMAND"
echo "---------------------"
echo "scp -rp s1220039@student.ssh.inf.ed.ac.uk:/afs/inf.ed.ac.uk/user/s12/s1220039/Documents/EXC/Assignment2/task$TASK/output $DIR/task$TASK/"
echo ""


