#!/bin/bash

newTask="think of a sample task"
echo $newTask >> ~/task_database.txt

newTask="when you see this the task text has been expanded"

# double quotes are expanded, single are not
echo $newTask
echo "$newTask"
echo '$newTask'

echo "------------"
echo "first arg: $1"
echo "============"
echo "first arg: $2"
echo "============"
echo "first arg: $3"

newTask=$1
echo "$newTask"

